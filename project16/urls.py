"""project16 URL Configuration

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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/',table,name='table'),
    path('forms/',forms,name='forms'),
    path('image/',image,name='image'),
    path('lists/',lists,name='lists'),
    path('formatting/',formatting,name='formatting'),
    path('anchor/',anchor,name='anchor'),
    path('marquee/',marquee,name='marquee'),
    path('colspan/',colspan,name='colspan'),
    path('nestedtable/',nestedtable,name='nestedtable'),
    path('rowspan/',rowspan,name='rowspan'),
]
