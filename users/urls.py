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
    url(r'^register/$', views.UserCreate.as_view(), name='register'),
    path('sendemail/', views.Reset_Passward.as_view(), name='reset_passward'),
    path('setnewpassword/<userReset>', views.Resetpassword.as_view(), name='resetpassword'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('uploadprofile/', views.ProfileUpload.as_view(), name='upload_profile'),
    path('login/', views.Login.as_view(), name='users'),
    path('reset/<str:id>/', views.reset_password, name='reset_password'),
    path('active/<str:short_id>/', views.activate, name='activate'),
    path('readprofile/<str:bucket>/<str:object_name>/', views.read_profile, name='read_profile'),
    path('new/', views.access_token, name='social'),
    path('sociallogin/', views.social_login, name='url'),
    url(r'^socialauth/$', views.SocialSignUp.as_view(),
        name='api-social-auth-register'),
]
