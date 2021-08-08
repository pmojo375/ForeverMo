from django.contrib import admin
from main.models import *
from import_export import resources

class GuestAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')


class PlusOneAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'host_name', 'host')
    
    def host_name(self, x):
        return x.host.firstname + ' ' + x.host.lastname
    host_name.short_description = 'Host Name'


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'title')


class MessageResource(resources.ModelResource):

    class Meta:
        model = Message


admin.site.register(Guest, GuestAdmin)
admin.site.register(PlusOne, PlusOneAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Song, SongAdmin)
