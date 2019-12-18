from django.db import models


# Create your models here.
# insert into axf_foodtype(typeid,typename,childtypenames,typesort) values("104749","热销榜","全部分类:0",1)
class AxfFoodType(models.Model):
    typeid = models.CharField(max_length=64)
    typename = models.CharField(max_length=64)
    childtypenames = models.CharField(max_length=128)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtype'


class AxfGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=256)
    productname = models.CharField(max_length=256)
    productlongname = models.CharField(max_length=256)
    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    marketprice = models.DecimalField(max_digits=6, decimal_places=2)
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=256)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'
