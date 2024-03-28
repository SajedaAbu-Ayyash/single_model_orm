from django.shortcuts import HttpResponse
from users_app import models

def index(request):
    # models.create_user()
    models.all_users()
    return HttpResponse('hello')

# Create your views here.
