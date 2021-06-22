from django.shortcuts import render
from django.core.mail import send_mail
from .models import Project
from django.conf import settings
from .forms import ContactForm
# Create your views here.
def home(request):
	projects=Project.objects.all()
	form=ContactForm(request.POST or None)
	context={'projects':projects,'form':form}

	if form.is_valid():
		name=form.cleaned_data['Name']
		message=form.cleaned_data['Message']
		mobile=form.cleaned_data['Mobile_No']
		subject='Message from Mysite'
		emailFrom=form.cleaned_data['Email']
		emailTo=settings.EMAIL_HOST_USER
		message='Name:%s\n%s\nMobile:%s\nMessage:%s'%(name,emailFrom,mobile,message)
		autoReply_subject='This is an Auto Reply'
		autoReply_message='Dear %s\n\nThank you for contacting me. Your message is important to Me and I will respond as soon as possible.\n\nKind Regards,\nDikshu Jain'%(name)
		send_mail(subject,message,emailFrom,[emailTo],fail_silently=True)	
		send_mail(autoReply_subject,autoReply_message,emailTo,[emailFrom],fail_silently=True)
		confirm_message="Thanks for the message. We will get right back to you."
		context={'projects':projects,'confirm_message':confirm_message}
	

	template='home.html'
	return render(request,template,context)