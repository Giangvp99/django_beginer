from .views import SignUpView
from django.urls import path

app_name = "users"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
