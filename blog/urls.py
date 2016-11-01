from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), #означает, что Django возьмет все, что придется на эту часть строки и передаст представлению в качестве переменной pk , [0-9] означает, что допустимы только цифры (от 0 до 9), но не буквы , + означает, что цифр должно быть от одной и больше , pk сокращение от primary key
]