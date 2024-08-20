from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),  # URL pattern for signup page 
    path('login/', LoginView.as_view(), name='login'),  # URL for login page
    path('logout/', LogoutView.as_view(), name='logout'),  # URL for logout page 
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),  # URL for requesting a password reset
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),  # Confirmation page after password reset email is sent
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # URL for resetting the password
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Confirmation page after the password is successfully reset
    path('profile/', views.profile_view, name='profile'),  # URL pattern for the profile page
]
