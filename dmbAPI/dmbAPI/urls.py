"""dmbAPI URL Configuration

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
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView

import blog.urls as blogUrls
import bank_rates.urls as bankRatesUrls

from contact_us import views

routeLists = [
    blogUrls.routeList,
    bankRatesUrls.routeList,
]

router = DefaultRouter()
for routeList in routeLists:
    for route in routeList:
        router.register(prefix=route[0], viewset=route[1], base_name=route[2])

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^new_financing/', TemplateView.as_view(template_name="new_financing.html")),
    url(r'^refinancing/', TemplateView.as_view(template_name="refinancing.html")),
    url(r'^contact/$', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}), ]
