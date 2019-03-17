from django.db import models

from users.models import Users


# Create your models here.

class UsersLocation(models.Model):
    id = models.fields.BigAutoField(primary_key=True, serialize=True, auto_created=True)
    userId = models.BigIntegerField()
    latitude = models.FloatField(max_length=21, default=00.000000)
    longitude = models.FloatField(max_length=21, default=00.000000)
    area = models.TextField(null=False, default='')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users_location"
        verbose_name_plural = "Users Location"
