from django.forms import ModelForm, TextInput
from .models import Mail, Mail2

class MailForm(ModelForm):
    
    class Meta:
        model = Mail
        fields = ['mail', 'name']
        widgets = {
            'mail' : TextInput(attrs={'class':'input','placeholder':'example@example.com'}),
            'name' : TextInput(attrs={'class': 'input', 'placeholder':'name'})
        }


class MailForm2(ModelForm):
    
    class Meta:
        model = Mail2
        fields = ['mail2', 'name2']
        widgets = {
            'mail2' : TextInput(attrs={'class':'input','placeholder':'example@example.com2'}),
            'name2' : TextInput(attrs={'class': 'input', 'placeholder':'name2'})
        }
