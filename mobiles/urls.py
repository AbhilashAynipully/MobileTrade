from django.urls import path
from .import views

urlpatterns = [
    path('search-mobiles/', views.get_all_mobiles, name='all_mobiles'),
    path('add-mobiles/', views.get_add_mobiles, name='add_mobiles'),
    path('delete-mobiles/<int:pk>/', views.get_delete_mobiles, name='delete-mobiles'),
    path('edit-mobiles/<int:pk>/', views.get_edit_mobiles, name='edit-mobiles'),
    path('delete-favourites/<int:pk>/', views.get_delete_favourites, name='delete-favourites'),
    path('mobie/<int:pk>/', views.get_mobile_details, name='mobile-details'),
    path('toggle-favourites/<int:pk>/', views.toggle_favourites, name='toggle-favourites'),
]
