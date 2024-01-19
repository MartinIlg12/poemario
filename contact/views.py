from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    #print(f'Tipo de petición: {request.method} ')
    contact_form=ContactForm()
    if request.method == 'POST':
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            #Estructura
            email=EmailMessage(
                "Pensamientos del Alma: Mensaje nuevo de contacto",
                f"De {name} <{email}>\n\nEscribio:\n\n{message}",
                f"{email}",
                ["pensamientosdelalma@hotmail.com"],
                reply_to=[email]
            )
            #Envio
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

    return render(request,"contact/contact.html",{'contact_form':contact_form})