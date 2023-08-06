from django_keycloak.models import Realm, Client
from django_keycloak.keycloak import KeycloakAdmin
from django.contrib.auth.models import Permission, Group
from typing import List, Dict


class RolePermissionKeyclock:

    def __init__(self, realm: Realm):
        clients = Client.objects.filter(realm=realm).all()

        clients_ids = [client.client_id for client in clients]

        self.keycloak_admin = KeycloakAdmin(server_url=realm.url,
                                            username=realm.username_or_email,
                                            password=realm.password,
                                            realm_name=realm.name,
                                            client_id=realm.client_id,
                                            client_secret_key=realm.secret,
                                            auto_refresh_token=['get', 'put', 'post', 'delete'],
                                            verify=True)
        self.clients_ids = [self.keycloak_admin.get_client_id(client_id) for client_id in clients_ids]

        self.users = self.keycloak_admin.get_users({})

        self.permissions = Permission.objects.all()

        self.roles = Group.objects.all()

    def _create_permissions(self, permissions_names: List[str], client_roles: List[Dict], client_role_id: str) -> None:
        perm_names = [role['name'] for role in client_roles if role['name'].endswith('_permission')]
        create_permissions = [perm for perm in permissions_names if perm not in perm_names]
        for roleName in create_permissions:
            self.keycloak_admin.create_client_role(client_role_id=client_role_id,
                                                   payload={'name': roleName, 'clientRole': True})

    def _create_roles(self, client_roles: List[Dict], client_role_id: str) -> None:
        roles_info = []
        for rol in self.roles:
            permissions_names = ['%s_%s_%s' % (perm.content_type.app_label, perm.codename, 'permission') for perm in
                                 rol.permissions.all()]
            permissions_include = [dict(rol) for rol in client_roles if rol['name'] in permissions_names]
            roles_info.append({
                'name': '%s_%s' % (rol.name, 'role'),
                'permissions': permissions_include
            })
        roles_names = [role['name'] for role in client_roles if role['name'].endswith('_role')]
        create_roles = [rol for rol in roles_info if rol['name'] not in roles_names]
        update_roles = [rol for rol in roles_info if rol['name'] in roles_names]
        for rol in create_roles:
            self.keycloak_admin.create_client_role(client_role_id=client_role_id,
                                                   payload={'name': rol['name'], 'clientRole': True})
            self.keycloak_admin.add_composite_client_roles_to_role(client_role_id=client_role_id, role_name=rol['name'],
                                                                   roles=rol['permissions'])

        for rol in update_roles:
            roles_info = self.keycloak_admin.get_composite_client_roles_to_role(client_role_id=client_role_id,
                                                                                role_name=rol['name'])
            permissions_assign = [permission for permission in rol['permissions'] if
                                  permission['name'] not in [r['name'] for r in roles_info]]
            permissions_remove = [r for r in roles_info if
                                  r['name'] not in [permission['name'] for permission in rol['permissions']]]
            if permissions_assign:
                self.keycloak_admin.add_composite_client_roles_to_role(client_role_id=client_role_id,
                                                                       role_name=rol['name'], roles=permissions_assign)
            if permissions_remove:
                self.keycloak_admin.remove_composite_client_roles_to_role(client_role_id=client_role_id,
                                                                          role_name=rol['name'],
                                                                          roles=permissions_remove)

    def synchronize_permissions_roles(self):
        for client_id in self.clients_ids:
            client_roles = self.keycloak_admin.get_client_roles(client_id=client_id)
            permissions_names = ['%s_%s_%s' % (perm.content_type.app_label, perm.codename, 'permission') for perm in
                                 self.permissions]
            self._create_permissions(permissions_names=permissions_names, client_roles=client_roles,
                                     client_role_id=client_id)
            client_roles = self.keycloak_admin.get_client_roles(client_id=client_id)
            self._create_roles(client_roles=client_roles, client_role_id=client_id)
