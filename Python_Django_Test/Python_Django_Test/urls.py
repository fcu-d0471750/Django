"""Python_Django_Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Script_02.musics.views import Do_Defend,defendhome
from Script_02.aggression.views import *
from django.conf.urls.static import static
from django.conf import settings

# url(網址,該網址一進入要執行的事情)
urlpatterns = [
             url(r'^$',defendhome), # 首頁
             url(r'^defendend/', Do_Defend),  # defendend.html網址
             url(r'^attackpage/',attackhome), # attackpage網址
             url(r'^attackend/',Do_Attack) # attackend網址
        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)