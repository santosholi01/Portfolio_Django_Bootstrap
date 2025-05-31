from django import forms
from .models import contractmessage


class contractform(forms.ModelForm):
    class  Meta:
        model =contractmessage
        fields=['name', 'email', 'message']
        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your name', 'style':'background-color:#1e1e2f;'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your gmail address','style':'background-color:#1e1e2f;'}),
            'message':forms.Textarea(attrs={'class':'form-control', 'rows':5,'style':'background-color:#1e1e2f;', 'placeholder':'Ask anything you like to know about me or my work------'}),
        }