from django.conf.urls import url
from . import views

urlpatterns = [
    # ^ 开头 $结尾 获取views.index方法中对应的界面
    url(r'^index/$', views.index),
    # 命名捕获，url本身并不传值，而是根据url的正则表达式进行传值
    url(r'^article/(?P<article_id>[0-9]+)$', views.aticle_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action,name='edit_action'),
]
