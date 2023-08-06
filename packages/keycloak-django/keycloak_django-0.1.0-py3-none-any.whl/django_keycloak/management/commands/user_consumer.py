from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.db.models import Value
from django.db.models.functions import Concat
from kafka import KafkaConsumer
import json
from django.conf import settings
from django.contrib.auth import get_user_model
from kafka.consumer.fetcher import ConsumerRecord


def order_by_timestamp(record:ConsumerRecord):
    return record.timestamp

def to_boolean(value):
    if isinstance(value, str) and value.lower() in ['true', 'false']:
        return value.lower() == 'true'
    return value

class Command(BaseCommand):
    help = 'User change consumer kafka'
    running = True
    bootstrap_servers = ""
    refresh_time = 0
    mechanism = ""
    username = ""
    password = ""
    topic = ""
    group_id = ""
    attribute_fillable = []


    def add_arguments(self, parser):
        parser.add_argument('-b', '--bootstrap_servers', nargs='?', const=1, type=str,
                            default=settings.KEYCLOAK['KEYCLOAK_KAFKA_BOOTSTRAP_SERVERS'],
                            help='Define the bootstrap_servers kafka')
        parser.add_argument('-r', '--refresh_time', nargs='?', const=1, type=int,
                            default=settings.KEYCLOAK['KEYCLOAK_KAFKA_REFRESH_TIME'],
                            help='Consumer refresh time kafka')
        parser.add_argument('-m', '--mechanism', nargs='?', const=1, type=str,
                            default=settings.KEYCLOAK['KEYCLOAK_KAFKA_MECHANISM'], help='Define a mechanism kafka')
        parser.add_argument('-u', '--username', nargs='?', const=1, type=str,
                            default=settings.KEYCLOAK['KEYCLOAK_KAFKA_USERNAME'], help='Define a username kafka')
        parser.add_argument('-p', '--password', nargs='?', const=1, type=str,
                            default=settings.KEYCLOAK['KEYCLOAK_KAFKA_PASSWORD'], help='Define a password kafka')
        parser.add_argument('-t', '--topic', nargs='?', const=1, type=str,
                            default=settings.KEYCLOAK['KEYCLOAK_KAFKA_TOPIC'], help='Define a topic kafka')
        parser.add_argument('-g', '--group', nargs='?', const=1, type=str,
                            default=settings.KEYCLOAK['KEYCLOAK_KAFKA_TOPIC_GROUP'], help='Define a topic kafka')


    def handle(self, *args, **options):
        self.bootstrap_servers = options['bootstrap_servers']
        self.refresh_time = options['refresh_time']
        self.mechanism = options['mechanism']
        self.username = options['username']
        self.password = options['password']
        self.topic = options['topic']
        self.group_id = options['group']
        self.attribute_fillable = settings.KEYCLOAK.get('KEYCLOAK_KAFKA_ATRIBUTES_FILLABLE_USER', [])
        self.basic_consume_loop()


    def user_create(self, payload_data):
        payload = {}
        for config in self.attribute_fillable:
            if isinstance(config, tuple):
                if config[1].startswith('attributes'):
                    if 'attributes' in payload_data['representation'] and config[1].replace('attributes.', '') in \
                            payload_data['representation']['attributes']:
                        payload[config[0]] = \
                            to_boolean(
                                payload_data['representation']['attributes'][config[1].replace('attributes.', '')][0])
                else:
                    payload[config[0]] = to_boolean(payload_data['representation'][config[1]])
                continue
            payload[config] = payload_data['representation'][config]
        payload['id'] = payload_data['user_id']
        UserModel = get_user_model()
        user = UserModel(**payload)
        user.save()


    def client_role_mapping_create(self, payload_data):
        client_id = payload_data['client_id']
        if client_id in settings.KEYCLOAK['CLIENT_ID_VALIDS']:
            payload_data['representation'] = payload_data['representation'][0]
            UserModel = get_user_model()
            user = UserModel.objects.get(pk=payload_data['user_id'])
            name = payload_data['representation']['name']
            if name.endswith('_role'):
                group = Group.objects.get(name=name.replace('_role',''))
                group.user_set.add(user)
            else:
                queryset = Permission.objects.annotate(
                    search_permission=Concat('content_type__app_label', Value('_'), 'codename'))
                permissions_available = list(queryset.filter(search_permission=name.replace('_permission','')))
                for perm in permissions_available:
                    perm.user_set.add(user)


    def user_delete(self, payload_data):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(pk=payload_data['user_id'])
            user.delete()
        except Exception as e:
            print('user not exist %s' % str(e))


    def client_role_mapping_delete(self, payload_data):
        client_id = payload_data['client_id']
        if client_id in settings.KEYCLOAK['CLIENT_ID_VALIDS']:
            payload_data['representation'] = payload_data['representation'][0]
            UserModel = get_user_model()
            user = UserModel.objects.get(pk=payload_data['user_id'])
            name = payload_data['representation']['name']
            if name.endswith('_role'):
                group = Group.objects.get(name=name.replace('_role', ''))
                group.user_set.remove(user)
            else:
                queryset = Permission.objects.annotate(
                    search_permission=Concat('content_type__app_label', Value('_'), 'codename'))
                permissions_available = list(queryset.filter(search_permission=name.replace('_permission', '')))
                for perm in permissions_available:
                    perm.user_set.remove(user)


    def user_update(self, payload_data):
        UserModel = get_user_model()
        user = UserModel.objects.get(pk=payload_data['user_id'])
        payload = {}
        for config in self.attribute_fillable:
            if isinstance(config, tuple):
                if config[1].startswith('attributes'):
                    if 'attributes' in payload_data['representation'] and config[1].replace('attributes.', '') in \
                            payload_data['representation']['attributes']:
                        payload[config[0]] = \
                            to_boolean(
                                payload_data['representation']['attributes'][config[1].replace('attributes.', '')][0])
                else:
                    payload[config[0]] = to_boolean(payload_data['representation'][config[1]])
                continue
            payload[config] = payload_data['representation'][config]
        for key, value in payload.items():
            setattr(user, key, value)
        user.save()


    def client_role_mapping_update(self, payload):
        print('update_role_permission no implementable')
        print(payload)


    def basic_consume_loop(self):
        consumer = None
        try:
            consumer = KafkaConsumer(self.topic,
                                     group_id=self.group_id,
                                     bootstrap_servers=self.bootstrap_servers.split(','),
                                     consumer_timeout_ms=self.refresh_time)

            while self.running:
                list_messages = [message for message in consumer]
                list_messages.sort(key=order_by_timestamp)
                call_methods = {
                    "USER_CREATE": self.user_create,
                    "CLIENT_ROLE_MAPPING_CREATE": self.client_role_mapping_create,
                    "USER_DELETE": self.user_delete,
                    "CLIENT_ROLE_MAPPING_DELETE": self.client_role_mapping_delete,
                    "USER_UPDATE": self.user_update,
                    "CLIENT_ROLE_MAPPING_UPDATE": self.client_role_mapping_update
                }
                for message in list_messages:
                    try:
                        message = json.loads(message.value.decode('utf-8'))
                        if 'resourceType' in message and 'operationType' in message and message['resourceType'] in ['USER', 'CLIENT_ROLE_MAPPING']:
                            method = "{}_{}".format(message['resourceType'], message['operationType'])
                            if 'representation' in message and isinstance(message['representation'], str):
                                message['representation'] = json.loads(message['representation'])
                                if 'attributes' in message['representation'] and isinstance(message['representation']['attributes'], str):
                                    message['representation']['attributes'] = json.loads(message['representation']['attributes'])
                            call_methods[method](message)
                            print(message)
                    except Exception as e:
                        print('error %s' % str(e))
        finally:
            # Close down consumer to commit final offsets.
            print('Close down consumer to commit final offsets.')
            if consumer:
                consumer.close()