from django.db import models


# Create your models here.

class Users(models.Model):
    id = models.fields.BigAutoField(primary_key=True, serialize=True, auto_created=True)
    username = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, default="")
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)
    isSuperuser = models.BooleanField(default=False)
    isStaff = models.BooleanField(default=False)
    isUser = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    dateJoined = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"
        verbose_name_plural = "users"
