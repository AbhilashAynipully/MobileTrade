from . import views
from django.urls import path

urlpatterns = [
    path('',views.get_home_page,name='home'),
]