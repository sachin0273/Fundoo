"""Fundoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls.static import static
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.admin.templatetags.admin_static import static

from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views

from Fundoo import settings

schema_view = get_swagger_view(title='Fundoo API')

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='users/social_login.html')),
    path('', include('users.urls')),
    path('api/', include('Note.urls')),
    path('', schema_view),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
