from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

# from axf.settings import APP_PRIVATE_KEY_STRING, ALIPAY_PUBLIC_KEY_STRING
from axf.settings import APP_PRIVATE_KEY_STRING, ALIPAY_PUBLIC_KEY_STRING
from cartApp.models import AxfCart
from cartApp.views import total
from orderApp.models import AxfOrder, AxfOrderGoods


# def order(request):
#     user_id = request.session.get('userId')
#
#     order = AxfOrder()
#     order.o_user_id = user_id
#     order.save()
#
#     total_price = total(user_id)
#
#     carts = AxfCart.objects.filter(c_user_id=user_id).filter(is_check=True)
#
#     for cart in carts:
#         orderGoods = AxfOrderGoods()
#         orderGoods.og_goods_id = cart.c_goods.id
#         orderGoods.og_order_id = order.id
#         orderGoods.goodNum = cart.goodsNum
#         orderGoods.save()
#         cart.delete()
#
#     order = AxfOrder.objects.get(pk=order.id)
#
#     orderGoods_list = order.axfordergoods_set.all()
#
#     context = {
#         'order': order,
#         'orderGoods_list': orderGoods_list,
#         'total': total_price,
#         'order_id': order.id
#
#     }
#
#     return render(request, 'axf/order/order.html', context=context)
#
#
# def address(request):
#     return render(request, 'axf/main/order/address.html')

def order(request):
    order_id = request.GET.get('order_id')

    order = AxfOrder.objects.get(pk=order_id)

    context = {
        'order': order,
        'total': order.axfordergoods_set.first().goodTotal
    }

    return render(request, 'axf/order/order.html', context=context)


def order_detail(request):
    user_id = request.session.get('userId')

    order = AxfOrder()

    order.o_user_id = user_id
    order.save()

    order = AxfOrder.objects.get(pk=order.id)

    carts = AxfCart.objects.filter(c_user_id=user_id).filter(is_check=True)
    print(carts)

    for cart in carts:
        ordergoods = AxfOrderGoods()
        ordergoods.og_order = order
        ordergoods.og_goods = cart.c_goods
        ordergoods.goodNum = cart.goodsNum
        ordergoods.goodTotal = total(user_id)
        ordergoods.save()
        cart.delete()

    data = {
        'msg': 'ok',
        'status': 200,
        'order_id': order.id
    }
    return JsonResponse(data=data)


def testPay(request):

    user_id = request.session.get('userId')

    order = AxfOrder.objects.filter(o_user_id=user_id).last()

    orderGoods = order.axfordergoods_set.all().first()

    alipay = AliPay(
        appid="2016101200665575",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=APP_PRIVATE_KEY_STRING,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=ALIPAY_PUBLIC_KEY_STRING,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False  # 默认False
    )

    subject = "爱鲜蜂购物订单"

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order.id,
        total_amount=orderGoods.goodTotal,
        subject=subject,
        return_url="https://www.baidu.com",
        notify_url="https://www.baidu.com"  # 可选, 不填则使用默认notify url
    )

    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)
