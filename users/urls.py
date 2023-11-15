from . import views
from django.urls import path

urlpatterns = [
    path('',views.get_home_page,name='home'),
    path('login',views.get_login_page,name='login'),
    path('logout',views.get_logout_page,name='logout'),
    path('register',views.get_register_page,name='register'),
    path('profile/<int:pk>',views.get_user_profile,name='profile'),
    path('delete-account',views.delete_account,name='delete-account'),
]