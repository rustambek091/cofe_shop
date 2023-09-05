from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import *
# Create your views here.
def Home(request):
    sarlavha = Sarlavha.objects.all()
    menu = Menu.objects.all()
    contact = Contact.objects.all()
    if request.method == "POST":
        
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message = message)
        contact.save()

    context = {
        'sarlavha':sarlavha,
        'menu':menu ,  
        'contact' : contact  
    }
    
    return render(request, 'index.html', context)

