from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages
from .models import Contact

# Create your views here.
def index(request):
    #context = {
        #"variable1":"Piyush is great",
        #"variable2":"harry is great"
                #}
    return render(request, 'index.html') #,context
    #return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Profile details has been Sent !')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")

def userdata(request):
    all_myapp = Contact.objects.all
    return render(request, 'userdata.html',{'all':all_myapp})