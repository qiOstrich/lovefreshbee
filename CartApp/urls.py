from django.conf.urls import url

from CartApp import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
    url(r'^addGoods/',views.addGoods,name='addGoods'),
    url(r'^subGoods/',views.subGoods,name='subGoods'),
    url(r'^changeStatus/',views.changeStatus,name='changeStatus'),
    url(r'^changeAll/',views.changeAll,name='changeAll'),
]
