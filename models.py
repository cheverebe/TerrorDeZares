from django.db import models

class Person(models.Model):
    full_name = models.TextField(max_length=500, blank=False, null=False)
    dni = models.TextField(max_length=500, blank=False, null=False)

class Sender(Person):
    pass

class Teacher(Sender):
    pass

class Division(models.Model):
    teacher = models.ForeignKey(Teacher, null=False, related_name='divisions')

class Event(models.Model):
    name = models.TextField(max_length=500, blank=False, null=False)

class Campaign(models.Model):
    name = models.TextField(max_length=500, blank=False, null=False)
    event = models.ForeignKey(Event, null=True, related_name='campaigns')

class Destinatary(Person):
    phoneNumber = models.TextField(max_length=500, blank=False, null=False)

class Student(Destinatary):
    division = models.ForeignKey(Division, null=False, related_name='students')

class Message(models.Model):
    content = models.TextField(max_length=500, blank=False, null=False)
    destinataries = models.ManyToManyField(Destinatary, related_name='messages')
    sender = models.ForeignKey(Sender, null=False, related_name='messages')