from django.conf.urls import url

from UserApp import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^checkName/', views.checkName, name='checkName'),
    # url(r'^sendMail/', views.sendMail, name='sendMail'),
    url(r'^activeUser/', views.activeUser, name='activeUser'),
    url(r'^get_code/', views.get_code, name='get_code'),

]
