import random
import uuid
from _md5 import md5
from io import BytesIO

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse

from LoveFirstBee import settings
from UserApp.models import Users
from UserApp.views_containter import send_email


def register(request):
    if request.method == 'GET':
        return render(request, 'lovefirstbee/user/register/register.html')
    if request.method == 'POST':
        name = request.POST.get('userid')
        email = request.POST.get('email')
        password = request.POST.get('userpwd')
        icon = request.FILES.get('headimg')

        user = Users.objects.filter(name=name)
        token = uuid.uuid4()

        password = make_password(password)

        # check_password(password,user.userpassword) 登录判断
        if user.count() == 0:
            adduser = Users()
            adduser.name = name
            adduser.email = email
            adduser.password = password
            adduser.icon = icon
            adduser.usertoken = token
            adduser.save()

            # cache.set(token, adduser.id, timeout=1800)

            # send_email(name=name, email=email, token=token)
            print("We don't send email and create cache.")
        else:
            return HttpResponse('服务器维护中……')

        return redirect(reverse('userApp:login'))


def checkName(request):
    data = {
        'msg': '√用户名可用',
        'status': 200,
    }

    name = request.GET.get('name')
    has_user = Users.objects.filter(name=name)

    if has_user.count() > 0:
        data['msg'] = '×用户名已经被占用'
        data['status'] = 201

    return JsonResponse(data=data)


# def sendMail(request):
#     # subject, message, from_email, recipient_list,html_message
#     subject = '标题'
#     message = 'yes'
#     # html_message = '准备激活'
#     # loader.get_template('lovefirstbee/send_mail/send_mail.html').render()
#     from_email = '951850464@qq.com'
#     recipient_list = ['951850464@qq.com', ]
#     send_mail(subject=subject,
#               message=message,
#               # html_message=html_message,
#               from_email=from_email,
#               recipient_list=recipient_list,
#               )
#
#     return HttpResponse('<h1>好的</h1>')


def activeUser(request):
    token = request.GET.get('token')

    user_id = cache.get(token)

    if user_id:
        user = Users.objects.get(pk=user_id)

        user.userstatus = 1
        user.save()

        cache.delete(token)

        return HttpResponse('<h1>激活成功</h1>')
    else:
        return HttpResponse('邮箱激活时间已过，请重新发送请求')


def login(request):
    if request.method == 'GET':
        context = {
            'msg': '请输入验证码'
        }
        return render(request, 'lovefirstbee/user/login/login.html', context=context)

    if request.method == 'POST':
        checkcode = request.POST.get('checkcode')

        verify_code = request.session.get('verify_code')

        import re

        result = re.search(verify_code, checkcode, re.IGNORECASE)
        if result:

            name = request.POST.get('userid')
            users = Users.objects.filter(name=name)
            if users.count() > 0:
                user = users.first()
                password = request.POST.get('userpwd')

                if check_password(password, user.password):

                    if user.userstatus:
                        request.session['userid'] = user.id
                        return redirect(reverse('mineApp:mine'))
                    else:
                        context = {
                            'msg': '用户未激活,请前往激活',
                        }
                        return render(request, 'lovefirstbee/user/login/login.html', context=context)

                else:
                    context = {
                        'msg': '用户名或密码错误',
                    }
                    return render(request, 'lovefirstbee/user/login/login.html', context=context)
            else:
                context = {
                    'msg': '用户名或密码错误',
                }
                return render(request, 'lovefirstbee/user/login/login.html', context=context)

        else:
            context = {
                'msg': '验证码输入错误',
            }
            return render(request, 'lovefirstbee/user/login/login.html', context=context)


def get_code(request):
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code
