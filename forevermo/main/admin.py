from django.contrib import admin
from main.models import *

class GuestAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'food', 'corn')
    def food(self, x):
        if x.foodchoice == 1:
            return 'Serloin'
        if x.foodchoice == 2:
            return 'Ahi Tuna'
        if x.foodchoice == 3:
            return 'Vegetarian'
        if x.foodchoice == 0:
            return 'Pork Tenderloin'
        else:
            return 'fail'
        food.short_description = 'Food Choice'
class PlusOneAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'food', 'host_name', 'corn', 'host')
    def food(self, x):
        if x.foodchoice == 1:
            return 'Serloin'
        if x.foodchoice == 2:
            return 'Ahi Tuna'
        if x.foodchoice == 3:
            return 'Vegetarian'
        if x.foodchoice == 0:
            return 'Pork Tenderloin'
        else:
            return 'fail'
    food.short_description = 'Food Choice'
    def host_name(self, x):
        return x.host.firstname + ' ' + x.host.lastname
    host_name.short_description = 'Host Name'
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'title')

admin.site.register(Guest, GuestAdmin)
admin.site.register(PlusOne, PlusOneAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Song, SongAdmin)
