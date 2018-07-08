from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = 'accountapp'

urlpatterns = [
     url(r'login/$',auth_views.LoginView.as_view(template_name='accountapp/login.html'), name='login'),
     url(r'logout/$',auth_views.LogoutView.as_view(), name='logout'),
     url(r'signup/$',views.Signup.as_view(), name='signup'),
]
