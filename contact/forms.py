from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Escribe tu Nombre'}
    ))
    email=forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Escribe tu Email'}
    ))
    message=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
         attrs={'class':'form-control','rows':2,'placeholder':'Escribe tu Mensaje'}
    ), min_length=10, max_length=1000)