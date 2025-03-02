from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library
from django.contrib.auth import login, logout, authenticate # this and the next two for user authentications
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test # for user (specific group) authentication 


def list_books(request):
    """Function-based view to list all books in the database."""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def user_login(request):
    """Handles user login functionality."""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home or another page
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def user_logout(request):
    """Handles user logout functionality."""
    logout(request)
    return render(request, "relationship_app/logout.html")

def register(request):
    """Handles user registration functionality."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def check_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def check_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
@user_passes_test(check_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
