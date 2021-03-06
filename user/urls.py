from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path, reverse_lazy

from user.views import district_by_county, register, school_by_district, verify

app_name = 'user'

urlpatterns = [
    # Registrácia a prihlásenie
    path('register/', register, name='register'),
    path('verify/<str:uidb64>/<str:token>/', verify, name='verify'),

    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Filtrovanie v registračnom formulári
    path('district/<int:pk>/', district_by_county, name='filter-district'),
    path('school/<int:pk>/', school_by_district, name='filter-school'),

    # Obnovenie hesla
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='user/password_reset.html',
             success_url=reverse_lazy('user:password-reset-done'),
             email_template_name='user/emails/password_reset.html'),
         name='password-reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html',
             success_url=reverse_lazy('user:password-reset-complete')),
         name='password-reset-confirm'),

    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'),
         name='password-reset-done'),

    # Zmena hesla
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'),
         name='password-reset-complete'),

    path('password-change/',
         PasswordChangeView.as_view(
             template_name='user/password_change.html',
             success_url=reverse_lazy('user:password-change-done')),
         name='password-change'),

    path('password-change/done/',
         PasswordChangeDoneView.as_view(
             template_name='user/password_change_done.html'),
         name='password-change-done'),
]
