from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from cartApp.models import AxfCart


def cart(request):
    # user_id = request.session.get('userId')
    # if user_id:

    user = request.user

    carts = AxfCart.objects.filter(c_user_id=int(user.id))

    is_true = True
    if carts.count() == 0:
        is_true = False
    for cart in carts:
        if not cart.is_check:
            is_true = False

    context = {
        'carts': carts,
        'is_true': is_true,
        'total': total(user)
    }

    return render(request, 'axf/main/cart/cart.html', context=context)
    # else:
    #     return render(request, 'axf/user/login/login.html')


def total(user_id):
    carts = AxfCart.objects.filter(c_user_id=user_id).filter(is_check=1)
    total = 0
    for cart in carts:
        total = total + cart.goodsNum * cart.c_goods.price

    return '%.2f' % total


def addToCart(request):
    # user_id = request.session.get('userId')
    data = {
        'msg': 'ok',
        'status': 200
    }
    # if user_id:

    user = request.user
    goods_id = request.GET.get('goodsId')
    carts = AxfCart.objects.filter(c_user_id=user.id).filter(c_goods_id=goods_id)
    if carts.count() > 0:
        cart = carts.first()
        cart.goodsNum = cart.goodsNum + 1

    else:
        cart = AxfCart()
        cart.c_user_id = user.id
        cart.c_goods_id = goods_id
        cart.goodsNum = 1

    cart.save()

    goodsNum = AxfCart.objects.get(c_goods_id=goods_id).goodsNum
    data['goodsNum'] = goodsNum

    data['total'] = total(user.id)

    return JsonResponse(data=data)

    # else:
    #     data['msg'] = '未登录'
    #     data['status'] = 201
    #     return JsonResponse(data=data)


def subToCart(request):
    user_id = request.session.get('userId')
    data = {
        'msg': 'ok',
        'status': 200
    }
    if user_id:
        goods_id = request.GET.get('goodsId')
        print(goods_id)
        carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goods_id)

        if carts.count() > 0:
            cart = carts.first()

            cart.goodsNum = cart.goodsNum - 1
            cart.save()
            is_have_goods = True
            if cart.goodsNum == 0:
                cart.delete()
                cart_list = AxfCart.objects.filter(c_user_id=user_id)
                if cart_list.count() == 0:
                    is_have_goods = False

            data['goodsNum'] = cart.goodsNum
            data['total'] = total(user_id)
            data['is_have_goods'] = is_have_goods
            return JsonResponse(data)
        else:
            data['msg'] = '购物车内没有该商品'
            data['status'] = 201
            return JsonResponse(data=data)
    else:
        data['msg'] = '用户未登录'
        data['status'] = 202
        return JsonResponse(data=data)


# 修改被被选中状态
def changeCheck(request):
    goods_id = request.GET.get('goodsId')

    goods = AxfCart.objects.get(c_goods_id=goods_id)
    goods.is_check = not goods.is_check
    goods.save()

    goods_list = AxfCart.objects.all()
    is_true = True
    for goods in goods_list:
        if not goods.is_check:
            is_true = False

    user_id = request.session.get('userId')

    data = {
        'msg': 'ok',
        'status': 200,
        'is_check': goods.is_check,
        'is_true': is_true,
        'total': total(user_id)
    }

    return JsonResponse(data=data)


# 修改全选状态
def changeAllCheck(request):
    display = request.GET.get('display')
    if display == 'none':
        goods_list = AxfCart.objects.filter(is_check=False)
        for goods in goods_list:
            goods.is_check = not goods.is_check
            goods.save()
    else:
        goods_list = AxfCart.objects.filter(is_check=True)
        for goods in goods_list:
            goods.is_check = not goods.is_check
            goods.save()
    data = {
        'msg': 'ok',
        'status': 200,
    }
    user_id = request.session.get('userId')
    data['total'] = total(user_id)
    return JsonResponse(data=data)
