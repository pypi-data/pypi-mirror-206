from django.contrib import admin

from django_keycloak.admin.realm import RealmAdmin
from django_keycloak.models import Realm

admin.site.register(Realm, RealmAdmin)
