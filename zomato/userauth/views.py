from django.shortcuts import render

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
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Perform registration logic here
        # For example, save the user to the database
        return render(request, "userauth/login.html", {"success": "Registration successful"})
    return render(request, "userauth/register.html")
