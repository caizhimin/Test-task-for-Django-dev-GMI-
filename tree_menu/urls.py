from django.conf.urls import url
from tree_menu import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<menu>.*)', views.allow_menu, name='allow_menu')
]