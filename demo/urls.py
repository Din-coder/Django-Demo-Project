"""demo URL Configuration

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
from django.conf.urls import url
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^welcome$', views.welcome, name='welcome'),
    url(r'^index$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^resetpassword$', views.resetpassword, name='resetpassword'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^loginpage$', views.loginpage, name='loginpage'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^usercreate$', views.usercreate, name='usercreate'),
    url(r'^userupdate/(?P<id>\d+)$', views.userupdate, name='userupdate'),
    url(r'^passupdate/(?P<id>\d+)$', views.passupdate, name='passupdate'),

    url(r'^create$', views.create, name='create'),
    url(r'^show$', views.show, name='show'),
    url(r'^delete/(?P<personid>\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<personid>\d+)$', views.edit, name='edit'),
    url(r'^update/(?P<personid>\d+)$', views.update, name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
