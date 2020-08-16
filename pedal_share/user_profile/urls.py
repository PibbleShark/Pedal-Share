from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'home'}, name='logout'),
    url(r'password-reset/', auth_views.PasswordResetView.as_view(template_name='user_profile'
                                                                               '/password_reset_form.html'),
        name='password_reset'),
    url(r'password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user_profile'
                                                                                        '/password_reset_done.html'),
        name='password_reset_done'),
    url(r'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name=
                                                                                'user_profile'
                                                                                '/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='user_profile'
                                                                                   '/password_reset_complete.html'),
        name='password_reset_complete'),
]

app_name = "user"
