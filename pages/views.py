from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Team
from cars.models import Cars
from django.core.mail import send_mail
from django.contrib.auth.models import User
def home(request):
  
    team = Team.objects.all()
    featured_cars= Cars.objects.order_by('-created_date').filter(is_featured=True)
    all_cars= Cars.objects.order_by('-created_date')
    model_search=Cars.objects.values_list('model',flat=True).distinct()
    city_search=Cars.objects.values_list('city',flat=True).distinct()
    year_search=Cars.objects.values_list('year',flat=True).distinct()
    body_style=Cars.objects.values_list('body_style',flat=True).distinct()
    data={
        'team':team,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style':body_style,
    }
    return render(request, 'index.html',data)

def about(request):
  
    team = Team.objects.all()
    data={
        'team':team
    }
    return render(request, 'pages/about.html',data)


def contact(request):
    if request.method=='POST':
        name= request.POST['name']
        subject= request.POST['subject']
        email= request.POST['email']
        phone= request.POST['phone']
        message= request.POST['message']
        email_subject = 'you are a new massage from carzone website regarding'
        message_body= 'name:'+name+'Email:'+email+'phone'+phone+'message'+message
        
        admin_info=User.objects.get(is_superuser=True)
        admin_email= admin_info.email
        send_mail(
        email_subject,
        message_body,
        'tomstark4200@example.com',
         [admin_email],
             fail_silently=False,
            )
        messages.success(request,'thank you for your contact,we will get back to you shortly')
        return redirect('contact')
    return render(request,'pages/contact.html')
def services(request):
  
    
    return render(request, 'pages/services.html')