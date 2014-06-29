from django.db import models


class Request(models.Model):
    get = models.TextField(max_length=500, blank=True, null=True)
    post = models.TextField(max_length=500, blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)