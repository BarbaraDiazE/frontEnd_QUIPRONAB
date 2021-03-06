"""QUIPRONAB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url

from Database.views import *

urlpatterns = [
    url(r"^$", ServerViews.as_view(), name="home page"),
    url(r"chemViewer2D/", A.as_view(), name="a"),
    url(r"renderStatic/", B.as_view(), name="render static"),
    url(r"render3D/", D.as_view(), name="3D"),
    url(r"inputchem/", InputChemStruc.as_view(), name="input chem struct"),
    url(r"about/", About.as_view(), name="about"),
    path("admin/", admin.site.urls),
]
