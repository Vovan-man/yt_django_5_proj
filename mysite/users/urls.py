from django.urls import path
from users import views
from django.contrib.auth.views import LoginView, LogoutView 
from .import views

app_name = "users"

urlpatterns = [
    #http://127.0.0.1:8000/users/
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/', views.profile, name='profile'),
    path('sellerprofile/<int:id>/', views.seller_profile, name="sellerprofile"),


]