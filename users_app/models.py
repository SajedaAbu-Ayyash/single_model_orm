from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    age = models.IntegerField()
    email_address = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


# # Create 3 users:
# def create_user():
#     User.objects.create(first_name = "Guevara", last_name = "Abu-Ayyash", email_address = 'guevara12@example.com', age = 21)
#     User.objects.create(first_name = "Sajeda", last_name = "Abu-Ayyash", email_address = 'sajeda@example.com', age = 25)
#     User.objects.create(first_name = "Mohannad", last_name = "Abu-Ayyash", email_address = 'mohannad@example.com', age = 27)
    
def add_user(first_name, last_name, email_address, age):
    User.objects.create(first_name = first_name, last_name = last_name, email_address = email_address, age = age)




