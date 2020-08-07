from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name="pages/index.html"), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password-reset/'
         '', auth_views.PasswordResetView.as_view
         (template_name='account/password_reset.html'),
         name="password_reset"),
    path('password-reset/done/'
         '', auth_views.PasswordResetDoneView.as_view
         (template_name='account/password_reset_done.html'),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>'
         '', auth_views.PasswordResetConfirmView.as_view
         (template_name='account/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('password-reset-complete/'
         '', auth_views.PasswordResetCompleteView.as_view
         (template_name='account/password_reset_complete.html'),
         name="password_reset_complete"),
    # path('activate/<str:uidb64>/<str:token' >, views.activate, name="activate"),

]
