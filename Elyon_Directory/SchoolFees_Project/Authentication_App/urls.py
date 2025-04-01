from django.urls import path
from .views import user_login, register, home, make_payment, view_receipt, about
from django.contrib.auth import views as auth_views  # Import Django's auth views


urlpatterns = [
    path('', about, name='about'),  # Default landing page
    path('home/', home, name='home'),  # Home page (will be protected in views)
    
    # Authentication paths
    path("login/", user_login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),

    # Payment and student info paths
    path('make-payment/', make_payment, name='make_payment'),
    path('view-receipt/', view_receipt, name='view_receipt'),
    # path('student-info/', student_info, name='student_info'),
]
