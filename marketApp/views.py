from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from marketApp.models import AxfFoodType, AxfGoods
from userApp.models import AxfUser


def market(request):
    typeid = request.GET.get('typeid', '104749')
    foodtypes = AxfFoodType.objects.all()

    childtypename = AxfFoodType.objects.get(typeid=typeid).childtypenames

    childtype_list = childtypename.split("#")

    typename_list = []

    for childtype in childtype_list:
        typename = childtype.split(":")
        typename_list.append(typename)

    childcid = int(request.GET.get('childcid', '0'))

    sort_rule_list = ['综合排序', '价格升序', '价格降序', '销量升序', '销量降序']

    sortRule = request.GET.get('sort_rule', '综合排序')

    childcid_goods = AxfGoods.objects.filter(categoryid=int(typeid)).filter(childcid=childcid)
    categoryid_goods = AxfGoods.objects.filter(categoryid=int(typeid))

    if childcid == 0:
        if sortRule == '价格升序':
            goods = categoryid_goods.order_by('price')
        elif sortRule == '价格降序':
            goods = categoryid_goods.order_by('-price')
        elif sortRule == '销量升序':
            goods = categoryid_goods.order_by('productnum')
        elif sortRule == '销量降序':
            goods = categoryid_goods.order_by('-productnum')
        else:
            goods = categoryid_goods
    else:
        if sortRule == '综合排序':
            if childcid:
                goods = childcid_goods
            else:
                goods = childcid_goods
        elif sortRule == '价格升序':
            goods = childcid_goods.order_by('price')
        elif sortRule == '价格降序':
            goods = childcid_goods.order_by('-price')
        elif sortRule == '销量升序':
            goods = childcid_goods.order_by('productnum')
        elif sortRule == '销量降序':
            goods = childcid_goods.order_by('-productnum')
        else:
            goods = categoryid_goods
    context = {
        'foodtypes': foodtypes,
        'goods': goods,
        'typeid': str(typeid),
        'typename_list': typename_list,
        'childcid': str(childcid),
        'sort_rule_list': sort_rule_list,
        'sortRule': sortRule,
    }


    return render(request, 'axf/main/market/market.html', context=context)
