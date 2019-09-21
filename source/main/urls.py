"""main URL Configuration

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
from django.contrib import admin
from django.urls import path
from webapp.views import entry_view, entry_create, entry_update, entry_delete, entry_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', entry_view, name='index'),
    path('entry/add/', entry_create, name='entry_add'),
    path('entry/edit/<int:pk>/', entry_update, name='entry_edit' ),
    path('entry/delete/<int:pk>/', entry_delete, name='entry_delete'),
    path('entry/search/', entry_search, name='search')
]
