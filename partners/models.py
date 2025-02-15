from django.db import models

# Create your models here.

class Partner(models.Model):
    name = models.CharField(max_length=255, )
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    organization = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Volunteer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(default='volunteer@gmail.com')
    phone_number = models.CharField(max_length=15)
    availability = models.CharField(max_length=255)
    skills = models.TextField()
    message = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"