from django.shortcuts import render

# Create your views here.
from HomeApp.models import Wheel, Nav, MustBuy, MainShow


def home(request):
    wheels = Wheel.objects.all()

    navs = Nav.objects.all()

    mustbuys = MustBuy.objects.all()

    mainshows = MainShow.objects.all()

    return render(request, 'lovefirstbee/main/home/home.html', context=locals())
