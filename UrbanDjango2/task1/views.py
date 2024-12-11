from http.client import HTTPResponse, error

from django.shortcuts import render
from django.template.context_processors import request

from task1.models import *



def sing_up(request):
    buyers = Buyer.objects.all()
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password == repeat_password and int(age)>=18 and username not in str(buyers):
            Buyer.objects.create(name = username, balance = 2000.0, age = age)
            return HTTPResponse(f'Добро пожаловать, {username}')

        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age)<18:
            info['error'] = 'Вам должно быть 18 лет или старше'
        elif username in str(buyers):
            info['error'] = 'Имя пользователя уже занято'
    return render(request, 'task1/registration_page.html', context=info)










# Create your views here.


