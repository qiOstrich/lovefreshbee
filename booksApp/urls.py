from django.conf.urls import url

from booksApp import views

urlpatterns=[
    url(r'^bookGoods/',views.bookGoods,name='bookGoods'),
]