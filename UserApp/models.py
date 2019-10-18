from django.db import models


# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    icon = models.ImageField(upload_to='%Y/%m/icon')

    usertoken = models.CharField(max_length=256)

    userstatus = models.NullBooleanField(default=False)

    class Meta:
        db_table = 'axf_user'
