from django.conf.urls import url
from . import views

urlpatterns = [
    # ^ 开头 $结尾 获取views.index方法中对应的界面
    url(r'^index/$', views.index),
]
