from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Item

def index(request):
    try:
        context = { 'first_name' : request.user.first_name }
        return render(request, 'index.html', context)         
    except AttributeError as e:
        return render(request, 'index.html')


def auf(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        print(user)
 
        if user is not None:
            print('auth success')
            login(request, user)
            return redirect('index')
        else:
            return JsonResponse({'status' : 'error'})
    else:
        return render(request, 'auf.html')

def reg(request):

    # Если приходит POST-запрос
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = email

        # Создаем пользователя
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        return JsonResponse({'status' : 'success'})
    return render(request, 'reg.html')
    

def logout_view(request):
    logout(request)
    return redirect('index') #перенаправление

def items_list (request):
    items = Item.objects.all(if santehnick_tupe == 'all':
                             good = Good.object.filter(santehnick_tupe = santehnick_tupe)
                             context = {})
    context = {
        'items_list' : items
    }
    return render (request, 'items_list.html', context)
