from typing import List
from django.conf import settings
from django.contrib.auth.models import Permission, Group
from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured


def set_profile(user, groups: List[Group], permissions: List[Permission]):
    user_groups = user.groups.all()
    user_permissions = user.get_user_permissions()
    add_groups = []
    add_permissions = []
    delete_groups = []
    delete_permissions = []
    
    for permission in user_permissions:
        if permission not in ['{}.{}'.format(p.content_type.app_label, p.codename) for p in permissions]:
            delete_permissions.append(permission)
            
    for group in user_groups:
        if group.name not in [g.name for g in groups]:
            delete_groups.append(group)
            
    for permission in permissions:
        if '{}.{}'.format(permission.content_type.app_label, permission.codename) not in [p for p in user_permissions]:
            add_permissions.append(permission)
            
    for group in groups:
        if group.name not in [g.name for g in user_groups]:
            add_groups.append(group)
    
    for group in add_groups:
        group.user_set.add(user)
        
    for permission in add_permissions:
        user.user_permissions.add(permission)

    for group in add_groups:
        group.user_set.remove(user)
        
    for permission in delete_permissions:
        data = permission.split('.')
        perm = Permission.objects.get(content_type__app_label=data[0],codename=data[1])
        perm.user_set.remove(user)
        
        
def get_user_model_keycloak():
    """
    Return the User Keycloak model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.KEYCLOAK['KEYCLOAK_USER_MODEL'], require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("KEYCLOAK_USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "KEYCLOAK_USER_MODEL refers to model '%s' that has not been installed" % settings.KEYCLOAK['KEYCLOAK_USER_MODEL']
        )