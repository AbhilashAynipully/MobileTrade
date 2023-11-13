from . import views
from django.urls import path

urlpatterns = [
    path('',views.get_home_page,name='home'),
    path('login',views.get_login_page,name='login'),
    path('logout',views.get_logout_page,name='logout'),
]