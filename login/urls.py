from django.conf.urls import url
from django.urls import path

from . import views
# from rest_framework_jwt.views import path
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^register/$', views.User_Create.as_view(), name='register'),
    path('loginpage/', views.Login.as_view(), name='loginpage'),
    path('Reset_Passward/', views.Reset_Passward.as_view(), name='Reset_Passward'),
    url(r'^activate/(?P<id>[\w.-]+)/$', views.activate, name='activate'),
    url(r'^reset_password/(?P<id>[\w.-]+)/$', views.reset_password, name='reset_password'),
    path('resetpassword/<userReset>', views.resetpassword.as_view(), name='resetpassword'),
    path('logout/', views.logout, name='logout'),
    path('hello/', views.HelloView.as_view(), name='hello')
]
