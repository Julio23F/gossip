from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, authenticate, logout

# Create your views here.
def login_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mdp = request.POST.get("mdp")
        user = authenticate(username=name, password=mdp)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")

User = get_user_model()

def register_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mdp = request.POST.get("mdp")
        user = User.objects.create_user(username=name, password=mdp)
        login(request, user)
        return redirect("home")

    return render(request, "register.html")

def logout_user(request):
    logout(request)
    return redirect("login")