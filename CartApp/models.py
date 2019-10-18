from django.db import models

# Create your models here.
from MarketApp.models import Goods
from UserApp.models import Users


class Cart(models.Model):
    c_goods = models.ForeignKey(Goods)
    c_user = models.ForeignKey(Users)

    c_goods_num = models.IntegerField(default=1)

    c_status = models.BooleanField(default=1)

    class Meta:
        db_table = 'axf_cart'
