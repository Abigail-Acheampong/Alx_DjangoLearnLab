from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("home")  # Change "home" to your actual homepage URL name
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    
    return render(request, "Authentication_App/login.html", {"form": form})

# Registration view
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, "Registration successful!")
            return redirect("home")  # Change "home" to your homepage URL
    else:
        form = UserRegisterForm()
    
    return render(request, "registration/register.html", {"form": form})

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    def get(self, request, *args, **kwargs):
        """Override GET request to allow logout via GET."""
        return self.post(request, *args, **kwargs)  # Call post method to log out the user

    def post(self, request, *args, **kwargs):
        """Perform logout and redirect to 'about' page."""
        return super().post(request, *args, **kwargs)
    

# About Page View (Redirect logged-in users to Home, this should not be it)
def about(request):
    if request.user.is_authenticated:
        return redirect("home")  # If logged in, go to home
    return render(request, "Authentication_App/about.html")

# Home Page (Only Accessible After Login)
@login_required
def home(request):
    return render(request, "Authentication_App/home.html")

# Payment Page (Restricted to Logged-in Users)
@login_required
def make_payment(request):
    return render(request, "Authentication_App/make_payment.html")

# Receipt Page (Restricted to Logged-in Users)
@login_required
def view_receipt(request):
    return render(request, "Authentication_App/view_receipt.html")

# Student Info Page (Restricted to Logged-in Users)
# @login_required
# def student_info(request):
#     return render(request, "/StudentInformation_App/student_list.html")