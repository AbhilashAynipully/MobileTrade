from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.get_home_page,name='home'),
    path('login',views.get_login_page,name='login'),
    path('logout',views.get_logout_page,name='logout'),
    path('register',views.get_register_page,name='register'),
    path('profile/<int:pk>',views.get_user_profile,name='profile'),
    path('delete-account',views.delete_account,name='delete-account'),
    path('profile-update',views.get_profile_update,name='profile-update'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
    template_name='password_reset.html'), name='password_reset'),
    path('password-reset/sent/', auth_views.PasswordResetDoneView.as_view(
    template_name='password_reset_sent.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    template_name='password_reset_complete.html'), name='password_reset_complete'),
]