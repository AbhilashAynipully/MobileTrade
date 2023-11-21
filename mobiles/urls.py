from django.urls import path
from .import views

urlpatterns = [
    path('search-mobiles/', views.get_all_mobiles, name='all_mobiles'),
    path('add-mobiles/', views.get_add_mobiles, name='add_mobiles'),
    path('delete-mobiles/<int:pk>/', views.get_delete_mobiles, name='delete-mobiles'),
]