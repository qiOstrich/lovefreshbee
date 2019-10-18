from django.shortcuts import render

# Create your views here.
from MarketApp.models import FoodTyep, Goods


def market(request):
    goodstypes = FoodTyep.objects.all()

    # goods = Goods.objects.all()[0:10]

    try:
        typeid = request.GET.get('typeid', 104749)
        childcid = request.GET.get('childcid')
        sortwith = request.GET.get('sort','0')
    except:
        typeid = 104749
        childcid = ''
        sortwith = '0'

    alltype_child = FoodTyep.objects.filter(typeid=typeid)[0].childtypenames

    childtypes = []
    try:
        types = alltype_child.split('#')
        for i in types:
            types = i.split(':')

            childtypes.append(types)
    except:
        types = alltype_child.split(':')
        childtypes.append(types)

    goods = Goods.objects.filter(categoryid=typeid)

    if childcid:
        goods = Goods.objects.filter(childcid=childcid)

        if sortwith == '1':
            goods = Goods.objects.filter(childcid=childcid).order_by('price')
        if sortwith == '2':
            goods = Goods.objects.filter(childcid=childcid).order_by('-price')
        if sortwith == '3':
            goods = Goods.objects.filter(childcid=childcid).order_by('productnum')
        if sortwith == '4':
            goods = Goods.objects.filter(childcid=childcid).order_by('-productnum')
    if not childcid:

        if sortwith == '1':
            goods = Goods.objects.filter(categoryid=typeid).order_by('price')
        if sortwith == '2':
            goods = Goods.objects.filter(categoryid=typeid).order_by('-price')
        if sortwith == '3':
            goods = Goods.objects.filter(categoryid=typeid).order_by('productnum')
        if sortwith == '4':
            goods = Goods.objects.filter(categoryid=typeid).order_by('-productnum')

    context = {
        'foodtype': goodstypes,
        'allgoods': goods,
        'typeid': str(typeid),
        'childcid': childcid,
        'childtypes': childtypes,
        'sort':sortwith,
    }

    return render(request, 'lovefirstbee/main/market/market.html/', context=context)
