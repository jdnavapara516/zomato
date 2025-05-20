from django.shortcuts import render
# import  User model 
from . import models


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Perform authentication logic here
        # For example, check if the username and password are valid
        if username == "admin" and password == "password":
            return render(request, "core/home.html")
        else:
            return render(request, "userauth/login.html", {"error": "Invalid credentials"})
    return render(request, "userauth/login.html")

def register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        print(f"Fullname: {fullname} Username: {username} Password1: {password1} Password2: {password2} Email: {email} Phone: {phone}")

        if password1 == password2:
            #enter data into user model
            user = models.User(
                username=username,
                password=password1,
                phon=phone,
                email=email
            )
            user.save()
        else:
            return render(request, "userauth/register.html", {"error": "Passwords do not match"})

        # Perform registration logic here
        # For example, save the user to the database
        return render(request, "userauth/login.html", {"success": "Registration successful"})
    return render(request, "userauth/register.html")



def data(request):
    users = models.User.objects.all()
    return render(request, "userauth/data.html", {"users": users})