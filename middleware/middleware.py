from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from userApp.models import AxfUser

LOGIN_REQUEST = [
    '/cartApp/cart/'
]

LOGIN_REQUEST_JSON = [
    '/cartApp/addToCart/',
    '/cartApp/subToCart/'
]


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):

        user_id = request.session.get('userId')

        if request.path in LOGIN_REQUEST:
            if user_id:
                user = AxfUser.objects.get(pk=user_id)
                request.user = user
            else:
                return redirect(reverse('userApp:login'))

        if request.path in LOGIN_REQUEST_JSON:
            if user_id:
                user = AxfUser.objects.get(pk=user_id)
                request.user = user
            else:
                data = {
                    'msg': '客户未登录',
                    'status': 201
                }
                return JsonResponse(data=data)

