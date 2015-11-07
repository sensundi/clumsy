"""unearthed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

print settings.STATIC_ROOT, settings.STATIC_URL
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitebrain/$', 'helian.views.index'),
    url(r'^dash/$', 'helian.views.dash'),
    url(r'^devices/$', 'helian.views.devices'),
    url(r'tables/$', 'helian.views.tables'),
    url(r'^viewdevices/(?P<dept>\w{0,50})/$', 'helian.views.getdevices'),
    url(r'^padlock/(?P<devid>\w{1,50})/$', 'helian.views.engagedevice'),
    url(r'^unlock/(?P<devid>\w{1,50})/$', 'helian.views.disengagedevice'),
    url(r'^update/(?P<devid>\w{1,50})/(?P<tmpr>\w+[.]\w+)/$', 'helian.views.updatetemperature'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
