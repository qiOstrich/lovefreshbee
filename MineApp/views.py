from django.shortcuts import render

# Create your views here.
from UserApp.models import Users


def mine(request):
    exit = request.GET.get('exit', 'none')

    if exit.lower() == 'yes':
        try :
            del request.session['userid']
        except:
            pass
        request.session.flush()
        exit = 'none'

    context = {
        'deflaut': 'block',
        'is_user': 'none',
        'register': 'block',
        'headimg': None,
        'user_name': '未登录',
        'exit': exit,
    }

    user_id = request.session.get('userid')

    if user_id:
        user = Users.objects.get(pk=user_id)

        context['deflaut'] = 'none'
        context['is_user'] = 'block'
        context['headimg'] = 'upload/' + str(user.icon)
        context['register'] = 'none'
        context['user_name'] = user.name
        context['exit'] = 'block'
    else:
        user_id = request.GET.get('userid', None)
        if user_id:
            user = Users.objects.get(pk=user_id)

            context['deflaut'] = 'none'
            context['is_user'] = 'block'
            context['headimg'] = 'upload/' + str(user.icon)
            context['register'] = 'none'
            context['user_name'] = user.name
            context['exit'] = 'block'

    return render(request, 'lovefirstbee/main/mine/mine.html', context=context)
