from django.conf.urls import url
from . import views

urlpatterns = [
    #^ 开头
    #$结尾
    url(r'^index/$', views.index)
]
