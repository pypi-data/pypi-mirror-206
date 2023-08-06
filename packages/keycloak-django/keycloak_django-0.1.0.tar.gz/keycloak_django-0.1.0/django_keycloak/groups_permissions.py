from django.contrib.auth.models import Group, Permission
from typing import List
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType


class GroupsPermissions:
    roles = []
    permissions = []

    def __init__(self, roles: List[str]) -> None:
        self.roles = [rol.replace('_role', '') for rol in list(
            set(roles)) if rol.endswith('_role')]
        self.permissions = [
            permission.replace('_permission', '') for permission in roles if permission.endswith('_permission')]

    def get_roles(self) -> List[Group]:
        # roles_available = list(Group.objects.filter(name__in=self.roles))
        roles_available = [Group(name=rol) for rol in self.roles]
        return roles_available

    def get_permissions(self) -> List[Permission]:
        # queryset = Permission.objects.annotate(search_permission=Concat('content_type__app_label', Value('_'), 'codename'))
        # permissions_available = list(queryset.filter(search_permission__in=self.permissions))
        ct = ContentType(app_label='permission', model='account')
        permissions_available = [Permission(
            name=permission, codename=permission, content_type=ct) for permission in self.permissions]
        return permissions_available

    def get_permissions_in_user(self) -> List[Permission]:
        # permissions_avalible = list([permision for permision in self.get_permissions() if permision.pk not in [
        #     permisions.pk for list_permisions in [list(rol.permissions.all()) for rol in self.get_roles()] for permisions in list_permisions]])
        return self.get_permissions()
