from django.db import models

class Guest(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

class PlusOne(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    host = models.OneToOneField(Guest, on_delete=models.CASCADE, primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

class Message(models.Model):
    name = models.CharField(max_length=80)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)

class Song(models.Model):
    title = models.CharField(max_length=80)
    artist = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
