"""Gym URL Configuration

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
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('main/',include('apps.main.urls')),
    path('contact/',include('apps.contact.urls')),
    path('account/',include('apps.account.urls')),
    path('blog/',include('apps.Blog.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header='پنل مدیریت باشگاه'
admin.site.index_title='ادمین عزیز به پنل مدیریت خوش آمدید'