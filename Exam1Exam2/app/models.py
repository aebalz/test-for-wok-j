from django.db import models

# Create your models here.


class Todo_list(models.Model):
    title = models.CharField(max_length=50, null=False)
    detail = models.TextField(null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


class Email(models.Model):
    email_address = models.EmailField(null=False)
    subject = models.CharField(max_length=50, null=False)
    detail = models.TextField(null=False)
    create_date = models.DateTimeField(auto_now_add=True)
