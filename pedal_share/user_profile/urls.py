from django.conf.urls import url
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    url(r'^register/$', views.register_view, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^detail/$', views.user_detail, name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_user, name='edit'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': 'home'}, name='logout'),
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]

app_name = "user"
