import uuid

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

import re

from django.urls import reverse
from django.utils.six import BytesIO

from userApp.models import AxfUser
from userApp.view_containt import sendEmail


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register/register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        emial = request.POST.get('emial')
        password = request.POST.get('password')
        password = make_password(password)
        img = request.FILES.get('img')

        user = AxfUser()

        user.u_name = name
        user.u_emial = emial
        user.u_password = password
        user.u_img = img
        token = uuid.uuid4()
        user.u_token = token

        user.save()

        cache.set(token, user.id, timeout=60)

        print(cache.get('token'))

        sendEmail(name, emial, token)

        return render(request, 'axf/user/login/login.html')


def login(request):
    if request.method == 'GET':
        is_active = True
        is_name = True
        is_password = True
        context = {
            'is_active': is_active,
            'is_name': is_name,
            'is_password': is_password
        }
        return render(request, 'axf/user/login/login.html', context=context)

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        code = request.POST.get('code')

        is_true = re.search(r'@', name)

        is_active = True
        is_name = True
        is_password = True
        context = {
            'msg': '用户名或密码不正确'
        }
        img_code = request.session.get('verify_code')
        code_is_true = re.search(code, img_code, re.IGNORECASE)
        if code_is_true:
            if not is_true:
                users = AxfUser.objects.filter(u_name=name)
            else:
                users = AxfUser.objects.filter(u_emial=name)
            print(users[0].u_active)
            if users.count() > 0:
                active = users[0].u_active
            else:

                return render(request, 'axf/user/login/login.html', context=context)

            if active == 0:
                context['msg'] = '用户尚未激活'
                context['name'] = name
                return render(request, 'axf/user/login/login.html', context=context)
            else:
                password_true = users[0].u_password

            if check_password(password, password_true):
                request.session['userId'] = users[0].id
                return redirect(reverse('mineApp:mine'))
            else:
                return render(request, 'axf/user/login/login.html', context=context)

        else:
            context['msg'] = '验证码输入错误'
            return render(request, 'axf/user/login/login.html', context=context)

        # if not is_true:
        #     users = AxfUser.objects.filter(u_name=name)
        #     if users.count() > 0:
        #         if users[0].u_active == 0:
        #             context['is_active'] = False
        #             return render(request, 'axf/user/login/login.html', context=context)
        #         else:
        #             if password == users[0].u_password:
        #                 return HttpResponse('登录成功')
        #             else:
        #                 return HttpResponse('密码不正确')
        #     else:
        #         context['is_name'] = False
        #         return render(request, 'axf/user/login/login.html', context=context)
        # else:
        #     users = AxfUser.objects.filter(u_emial=name)
        #     if users.count() > 0:
        #         if users[0].u_active == 0:
        #             context['is_active'] = False
        #             return render(request, 'axf/user/login/login.html', context=context)
        #         else:
        #             if password == users[0].u_password:
        #                 return HttpResponse('登录成功')
        #             else:
        #                 return HttpResponse('密码不正确')
        #     else:
        #         context['is_name'] = False
        #         return render(request, 'axf/user/login/login.html', context=context)


def checkname(request):
    print(request.method)
    name = request.GET.get('name')

    users = AxfUser.objects.filter(u_name=name)

    data = {
        'msg': '✓用户名正确',
        'status': 200
    }
    if users.count() > 0:
        data['msg'] = 'ㄨ用户名已存在'
        data['status'] = 201

    return JsonResponse(data=data)


def activeUser(request):
    token = request.GET.get('token')

    user_id = cache.get(token)

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        if user.u_token == token:
            user.u_active = 1
            user.save()
            cache.delete(token)
            return HttpResponse('激活成功')
        else:
            return HttpResponse('激活失败，请重新发送')
    else:
        return HttpResponse('链接已失效，请重新请求')


def active(request):
    name = request.GET.get('name')
    users = AxfUser.objects.filter(u_name=name)
    if users.count() > 0:
        token = users[0].u_token
        cache.set(token, users[0].id, timeout=60)
        sendEmail(users[0].u_name, users[0].u_emial, users[0].u_token)
        return redirect(reverse('userApp:login'))
    else:
        return HttpResponse('请求不合法')


def get_code(request):
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code
