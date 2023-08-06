# -*- coding: utf-8 -*-
from django.utils import timezone
from django.conf import settings
from django.http.response import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from .tools import get_user_model_keycloak, set_profile
from .keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakInvalidTokenError
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed, NotAuthenticated
from django.contrib.auth import get_user_model
from django_keycloak.models import keycloakUserAbstract
from django.contrib.auth import login
from django.contrib.auth import logout


class KeycloakMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        """
        :param get_response:
        """

        self.config = settings.KEYCLOAK

        # Read configurations
        try:
            self.server_url = self.config['SERVER_URL']
            self.client_id = self.config['CLIENT_ID']
            self.audience_client = self.config.get(
                'AUDIENCE_CLIENT', self.client_id)
            self.realm = self.config['REALM_NAME']
        except KeyError as e:
            raise Exception(
                "KEYCLOAK_SERVER_URL, KEYCLOAK_CLIENT_ID or KEYCLOAK_REALM not found.")

        self.client_secret_key = self.config.get('CLIENT_SECRET_KEY', None)
        self.client_public_key = self.config.get('PUBLIC_KEY', None)
        self.default_access = self.config.get('DEFAULT_ACCESS', "DENY")
        self.method_validate_token = self.config.get(
            'METHOD_VALIDATE_TOKEN', "INTROSPECT")
        self.keycloak_authorization_config = self.config.get(
            'AUTHORIZATION_CONFIG', None)
        self.client_id_valids = self.config.get('CLIENT_ID_VALIDS', [])
        self.create_user_if_not_exist = self.config.get(
            'CREATE_USER_IF_NOT_EXIST', False)
        self.attributes_fillable = self.config.get('ATTRIBUTES_FILLABLE', None)
        self.update_user_only_login = self.config.get(
            'UPDATE_USER_ONLY_LOGIN', None)
        self.method_create_user = self.config.get('CREATE_USER_METHOD', None)
        self.public_key_validate = self.config.get(
            'PUBLIC_KEY_VALIDATE', 'inter')

        # Create Keycloak instance
        self.keycloak = KeycloakOpenID(server_url=self.server_url,
                                       client_id=self.client_id,
                                       realm_name=self.realm,
                                       client_secret_key=self.client_secret_key,
                                       client_id_valids=self.client_id_valids)

        # Read policies
        if self.keycloak_authorization_config:
            self.keycloak.load_authorization_config(
                self.keycloak_authorization_config)

        # Django
        self.get_response = get_response

    def __call__(self, request):
        """
        :param request:
        :return:
        """
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Validate only the token introspect.
        :param request: django request
        :param view_func:
        :param view_args: view args
        :param view_kwargs: view kwargs
        :return:
        """

        if 'HTTP_AUTHORIZATION' not in request.META:
            return None

        token = request.META.get('HTTP_AUTHORIZATION')
        self.realm = self.config['REALM_NAME']

        try:
            user_groups, user_permissions, user_info = self.keycloak.get_roles_permissions_user(token.replace('Bearer ', ''),
                                                                                                public_key_validate=self.public_key_validate,
                                                                                                method_token_info=self.method_validate_token.lower(),
                                                                                                key=self.client_public_key, audience=self.audience_client)
        except KeycloakInvalidTokenError as e:
            logout(request=request)
            return JsonResponse({"detail": AuthenticationFailed.default_detail},
                                status=AuthenticationFailed.status_code)

        UserModel = get_user_model()

        try:
            print(user_info['sub'])
            user = UserModel.objects.get(id=user_info['sub'])
            print(user)
            print(user_groups)
            print(user_permissions)
            user.last_login = timezone.now()
            user.groups = user_groups
            user.permissions = user_permissions
            user.save()
            # if self.update_user_only_login and request.get_full_path() == self.update_user_only_login:
            #     set_profile(user, user_groups, user_permissions)

        except UserModel.DoesNotExist:
            # if self.method_create_user and self.method_create_user.to == 'KAFKA':
            #     return JsonResponse({"detail": AuthenticationFailed.default_detail},
            #                     status=AuthenticationFailed.status_code)
            # update_profile = False
            payload = {}
            for config in self.attributes_fillable:
                # if config in ["permissions", "groups"]:
                #     update_profile = True
                #     continue
                if isinstance(config, tuple):
                    payload[config[0]] = user_info[config[1]]
                    continue
                payload[config] = user_info[config]
            user = None
            if self.create_user_if_not_exist:
                user = UserModel(**payload)
                # if update_profile:
                #     set_profile(user, user_groups, user_permissions)
                # user.save()
                user.last_login = timezone.now()
                user.groups = user_groups
                user.permissions = user_permissions
                user.save()
            if user:
                login(request, user)
            else:
                User = get_user_model_keycloak()
                user = User(**payload)
                user.groups = user_groups
                user.permissions = user_permissions
                # if update_profile and isinstance(user, keycloakUserAbstract):
                #     user.permissions = user_permissions
                #     user.groups = user_groups

        request.user = user

        if self.default_access == "DENY" and not user_permissions and not user_groups:
            # User Permission Denied
            return JsonResponse({"detail": PermissionDenied.default_detail},
                                status=PermissionDenied.status_code)
        return None

    @property
    def keycloak(self):
        return self._keycloak

    @keycloak.setter
    def keycloak(self, value):
        self._keycloak = value

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value

    @property
    def server_url(self):
        return self._server_url

    @server_url.setter
    def server_url(self, value):
        self._server_url = value

    @property
    def update_user_only_login(self):
        return self._update_user_only_login

    @update_user_only_login.setter
    def update_user_only_login(self, value):
        self._update_user_only_login = value

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def create_user_if_not_exist(self):
        return self._create_user_ifnotexist

    @create_user_if_not_exist.setter
    def create_user_if_not_exist(self, value):
        self._create_user_ifnotexist = value

    @property
    def attributes_fillable(self):
        return self._atributes_fillable

    @attributes_fillable.setter
    def attributes_fillable(self, value):
        self._atributes_fillable = value

    @property
    def client_id_valids(self):
        return self._client_id_valids

    @client_id_valids.setter
    def client_id_valids(self, value):
        self._client_id_valids = value

    @property
    def audience_client(self):
        return self._audience_client

    @audience_client.setter
    def audience_client(self, value):
        self._audience_client = value

    @property
    def client_secret_key(self):
        return self._client_secret_key

    @client_secret_key.setter
    def client_secret_key(self, value):
        self._client_secret_key = value

    @property
    def client_public_key(self):
        return self._client_public_key

    @client_public_key.setter
    def client_public_key(self, value):
        self._client_public_key = value

    @property
    def realm(self):
        return self._realm

    @realm.setter
    def realm(self, value):
        self._realm = value

    @property
    def keycloak_authorization_config(self):
        return self._keycloak_authorization_config

    @keycloak_authorization_config.setter
    def keycloak_authorization_config(self, value):
        self._keycloak_authorization_config = value

    @property
    def method_validate_token(self):
        return self._method_validate_token

    @method_validate_token.setter
    def method_validate_token(self, value):
        self._method_validate_token = value

    @property
    def method_create_user(self):
        return self._method_create_user

    @method_create_user.setter
    def method_create_user(self, value):
        self._method_create_user = value
