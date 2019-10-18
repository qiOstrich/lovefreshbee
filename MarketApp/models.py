from django.db import models


# Create your models here.
class FoodTyep(models.Model):
    # insert
    # into
    # (typeid, typename, childtypenames, typesort)
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtype'


class Goods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=256)
    productname = models.CharField(max_length=64)
    productlongname = models.CharField(max_length=128)

    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=32)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()

    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=32)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


