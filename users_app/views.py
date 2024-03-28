from django.shortcuts import render, redirect
from . import models


def index(request):
    # models.create_user()
    # models.all_users()
    context = {
        'users' : models.User.objects.all()
    }
    return render(request, "index.html", context)

def add_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email_address = request.POST['email_address']
        age = request.POST['age']
    models.add_user(first_name, last_name, email_address, age)
    return redirect('/')

# Create your views here.
