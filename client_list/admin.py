from django.contrib import admin
from client_list.models import Client


class ClientAdmin(admin.ModelAdmin):

    pass

admin.site.register(Client, ClientAdmin)
