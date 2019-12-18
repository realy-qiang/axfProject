from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from userApp.models import AxfUser


def mine(request):
    user_id = request.session.get('userId', '')

    if user_id:
        user = AxfUser.objects.filter(pk=user_id)[0]
        img = user.u_img
        print(img)
        context = {
            'active': True,
            'img': img,
            'name':user.u_name
        }

        return render(request, 'axf/main/mine/mine.html', context=context)
    else:
        return render(request, 'axf/main/mine/mine.html')


def loginOut(request):
    request.session.flush()
    return redirect(reverse('mineApp:mine'))