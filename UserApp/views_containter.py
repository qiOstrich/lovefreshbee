from django.core.mail import send_mail
from django.template import loader


def send_email(name, email, token):
    name = name
    email = email
    token = token

    subject = '标题'
    message = 'yes'
    context = {
        'name':name,
        'url':'http://127.0.0.1:8000/userApp/activeUser/?token='+str(token)
    }

    html_message = loader.get_template('lovefirstbee/send_mail/send_mail.html').render(context=context)
    from_email = '951850464@qq.com'
    recipient_list = [email, ]
    send_mail(subject=subject,
              message=message,
              html_message=html_message,
              from_email=from_email,
              recipient_list=recipient_list,
              )
