from django.db import models


# Create your models here.
from marketApp.models import AxfGoods
from userApp.models import AxfUser


class AxfCart(models.Model):
    c_user = models.ForeignKey(AxfUser)
    c_goods = models.ForeignKey(AxfGoods)
    goodsNum = models.IntegerField()
    is_check = models.BooleanField(default=True)


    class Meta:
        db_table = 'axf_cart'
