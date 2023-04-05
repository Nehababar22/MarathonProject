"""Marathon_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from Marathon_App.routers import router
from django.contrib import admin
from django.urls import path,include,re_path
from Marathon_App import views 
from dj_rest_auth.views import LogoutView,PasswordResetView,PasswordResetConfirmView,PasswordChangeView
from Marathon_App.views import CustomLoginAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls,)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('login/',CustomLoginAPI.as_view()),
    path('logout/',LogoutView.as_view()),
    path('password-reset/',PasswordResetView.as_view(),  name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-change/', PasswordChangeView.as_view(),  name='password_change'),
    
]
