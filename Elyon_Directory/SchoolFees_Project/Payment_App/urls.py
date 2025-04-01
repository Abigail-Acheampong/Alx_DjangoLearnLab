from django.urls import path
from .views import register_payment, payment_list, get_students_by_grade

urlpatterns = [
    path("make_payment/", register_payment, name="make_payment"),
    path("payments/", payment_list, name="payment_list"),
    path("get-students/", get_students_by_grade, name="get_students"),
]
