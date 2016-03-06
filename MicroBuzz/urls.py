"""MicroBuzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace='social')),
    # Home URL
	url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
	# Logout URL
	url(r'^users/logout/$','django.contrib.auth.views.logout',{'next_page': '/'},name="user-logout"),

    
]
