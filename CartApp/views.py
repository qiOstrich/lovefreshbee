from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from CartApp.models import Cart
from MarketApp.models import Goods
from UserApp.models import Users


def cart(request):
    user_id = request.session.get('userid')

    if user_id:
        user = Users.objects.get(pk=user_id)

        if user:
            context = {
                'msg': 'OK',
                'status': 200,
                'user': user,
                'all_select': 1,

            }

            carts = Cart.objects.filter(c_user_id=user.id)

            if carts.count() > 0:
                context['carts'] = carts
                goods_list = []
                # cart_list = []
                # cart_list.append(cart)
                total_price = 0
                for member in carts:
                    goods = Goods.objects.get(pk=member.c_goods_id)
                    status = member.c_status
                    goods_and_num = (goods, member.c_goods_num, status)
                    goods_list.append(goods_and_num)
                    if member.c_status:
                        total_price = total_price + member.c_goods_num * goods.price

                    if not member.c_status:
                        context['all_select'] = 0

                context['total_price'] = round(total_price, 2)
                context['goods'] = goods_list
            else:
                context['goods'] = None

            return render(request, 'lovefirstbee/main/cart/cart.html', context=context)


    else:

        return redirect(reverse('userApp:login'))


def addGoods(request):
    data = {
        'msg': 'OK',
        'status': 200,
    }
    userid = request.session.get('userid')
    if userid:
        c_goods_id = request.GET.get('goodsid')
        carts = Cart.objects.filter(c_goods_id=c_goods_id).filter(c_user_id=userid)

        if carts.count() > 0:
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = Cart()
            cart.c_goods_id = c_goods_id
            cart.c_user_id = userid
        cart.save()
        data['goods_num'] = cart.c_goods_num

        total_price = 0
        all_carts = Cart.objects.filter(c_user_id=userid)

        for this_cart in all_carts:
            if this_cart.c_status:
                goods = Goods.objects.get(pk=this_cart.c_goods_id)
                total_price = total_price + this_cart.c_goods_num * goods.price
        data['total_price'] = round(total_price, 2)
    else:
        data['status'] = 201
        data['msg'] = '请先登录'

    return JsonResponse(data=data)


def subGoods(request):
    data = {
        'msg': 'OK',
        'status': 200,
    }
    userid = request.session.get('userid')

    if userid:
        c_goods_id = request.GET.get('goodsid')
        carts = Cart.objects.filter(c_goods_id=c_goods_id).filter(c_user_id=userid)

        if carts.count() > 0:
            cart = carts.first()
            if cart.c_goods_num > 1:
                cart.c_goods_num = cart.c_goods_num - 1
                cart.save()
                data['goods_num'] = cart.c_goods_num
            else:
                cart.delete()
                data['goods_num'] = 0
        total_price = 0
        all_carts = Cart.objects.filter(c_user_id=userid)

        for this_cart in all_carts:
            if this_cart.c_status:
                goods = Goods.objects.get(pk=this_cart.c_goods_id)
                total_price = total_price + this_cart.c_goods_num * goods.price
        data['total_price'] = round(total_price, 2)

    else:
        data['status'] = 201
        data['msg'] = '请先登录'

    return JsonResponse(data=data)


def changeStatus(request):
    data = {
        'msg': 'OK',
        'status': 200,
        'all_select': 1,
    }
    userid = request.session.get('userid')

    if userid:

        c_goods_id = request.GET.get('goodsid')

        carts = Cart.objects.filter(c_goods_id=c_goods_id).filter(c_user_id=userid)
        if carts.count() > 0:
            cart = carts.first()
            if cart.c_status:
                cart.c_status = 0
                data['c_status'] = 0
            else:
                cart.c_status = 1
                data['c_status'] = 1
            cart.save()

        all_carts = Cart.objects.filter(c_user_id=userid)
        total_price = 0
        for member in all_carts:
            if not member.c_status:
                data['all_select'] = 0
            else:
                goods = Goods.objects.get(pk=member.c_goods_id)
                total_price = total_price + member.c_goods_num * goods.price

        data['total_price'] = round(total_price, 2)
    return JsonResponse(data=data)


def changeAll(request):
    data = {
        'msg': 'OK',
        'status': 200,
    }
    userid = request.session.get('userid')
    all_select = request.GET.get('all_status')
    if all_select == '0':
        all_select = False
    else:
        all_select = True

    if userid:

        carts = Cart.objects.filter(c_user_id=userid)

        if carts.count() > 0:

            if all_select:
                for member in carts:
                    member.c_status = 0
                    member.save()
                data['all_select'] = 0

            else:
                for member in carts:
                    member.c_status = 1
                    member.save()
                data['all_select'] = 1

    total_price = 0
    carts = Cart.objects.filter(c_user_id=userid).filter(c_status=True)
    for member in carts:
        total_price = total_price + member.c_goods_num * member.c_goods.price
    data['total_price'] = round(total_price, 2)
    return JsonResponse(data=data)
