from django.urls import path
from .import views

urlpatterns = [
    path('search-mobiles/', views.get_all_mobiles, name='all_mobiles'),
]