from django.db import models

# Create your models here.
from cartApp.models import AxfCart
from marketApp.models import AxfGoods
from userApp.models import AxfUser


class AxfOrder(models.Model):
    o_user = models.ForeignKey(AxfUser)
    o_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'axf_order'


class AxfOrderGoods(models.Model):
    og_order = models.ForeignKey(AxfOrder)
    og_goods = models.ForeignKey(AxfGoods)
    goodNum = models.IntegerField()
    goodTotal = models.FloatField()

    class Meta:
        db_table = 'axf_ordergoods'


class AxfAddress(models.Model):
    address = models.CharField(max_length=256)
    tel = models.CharField(max_length=32)

    class Meta:
        db_table = 'axf_address'


class AxfOderAddress(models.Model):
    oa_order = models.OneToOneField(AxfOrder)
    oa_address = models.ForeignKey(AxfAddress)

    class Meta:
        db_table = 'axf_orderaddress'


