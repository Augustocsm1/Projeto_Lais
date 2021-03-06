"""Lais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from locais.api import viewsets as locaisviewsets
from atendimento.api import viewsets as atendimentoviewsets
from cidadao.api import viewsets as cidadaoviewsets


route = routers.DefaultRouter()
route.register(r'Locais', locaisviewsets.locaisViewset, basename="Locais")
route.register(r'Atendimento', atendimentoviewsets.atendimentoViewset, basename="Atendimento")
route.register(r'Cidadao', cidadaoviewsets.cidadaoViewset, basename="Cidadao")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('', include(route.urls))
]
