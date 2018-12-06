"""qidian URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from App import views

app_name = 'App'
urlpatterns = [
    url('^home/', views.home,name='home'),
    url('^register/', views.register,name='register'),
    url('^login/', views.login,name='login'),
    url('^unlogin/', views.unlogin, name='unlogin'),
    url('^upload_info/', views.upload_info, name='upload_info'),
    url('^upload_icon/', views.upload_icon, name='upload_icon'),
    url('^add_inovel/', views.add_inovel, name='add_inovel'),
    url('^test/', views.test, name='test'),
    url('^classify_inovel/', views.classify_inovel, name='classify_inovel'),
    url('^word_tip/', views.word_tip, name='word_tip'),
    # url('^find_jump/', views.find_jump, name='find_jump'),
    url('^return_data/', views.return_data, name='return_data'),

]
