from django.shortcuts import render

# Create your views here.
from CartApp.models import Cart
from UserApp.models import Users


def bookGoods(request):
    userid = request.session.get('userid')

    if userid:
        user = Users.objects.get(pk=userid)

        carts = Cart.objects.filter(c_user_id=userid).filter(c_status=True)


        print(userid)
        print(user)
        print(carts)
        context = {

        }
        return render(request, 'lovefirstbee/user/books/books.html', context=context)
