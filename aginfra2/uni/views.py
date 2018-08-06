from django.shortcuts import render
#from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from uni.forms import emailform
from django.core.mail import send_mail
from django.shortcuts import reverse
# Create your views here.

def IndexView(request):
    #template_name='uni/index.html'
    form=emailform()
    if request.method == 'POST':
        form=emailform(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data['name']))
            subject=form.cleaned_data['subject']
            sender=form.cleaned_data['email']
            body="Name:"+form.cleaned_data['name']+"\nEmail:"+form.cleaned_data['email']+"\n\n"+form.cleaned_data['message']
            to=['sunny004gupta@gmail.com']
            try:
                send_mail( subject, body, sender, to ,fail_silently=False)
                return HttpResponseRedirect(reverse('index'))
            except:
                print('Error sending message.\n********* \n'+body)
                return HttpResponseRedirect(reverse('index'))

    return render(request,'uni/index.html',context={'form':form})
