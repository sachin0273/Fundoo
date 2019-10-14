"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Purpose: in this urls module we created urls for all rest api in views and this will included in main url module
author:  Sachin Shrikant Jadhav
since :  25-09-2019
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""

from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^register/$', views.User_Create.as_view(), name='register'),
    path('Reset_Passward/', views.Reset_Passward.as_view(), name='Reset_Passward'),
    path('resetpassword/<userReset>', views.Resetpassword.as_view(), name='resetpassword'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('s3upload/', views.S3Upload.as_view(), name='s3'),
    path('login/', views.Login.as_view(), name='login'),
    path('r/<str:id>/', views.reset_password, name='reset_password'),
    path('a/<str:short_id>/', views.activate, name='activate'),
    path('S3read/<str:bucket>/<str:object_name>/', views.s3_read, name='s3'),
]
