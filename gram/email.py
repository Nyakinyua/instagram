from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name,receiver):
    #creating message subject to the sender
    subject = "Welcome to Nyakinyua Instapics, share photos and views photos from followers"
    sender = "jayjoys968@gmail.com"
    
    #passing in the context variables
    text_content = render_to_string('email/grampic.txt',{"name":name})
    html_content = render_to_string('email/gramemail.html',{"name":name})
    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
                                    