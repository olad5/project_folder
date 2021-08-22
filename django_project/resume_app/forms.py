from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        # specifies what the model to be used
        model = Contact
        # the model fields to use
        fields = ("contact_name", "subject", "from_email", "message")

        # Widgets that show how the form should be displayed
        widgets = {

            'contact_name': forms.TextInput(attrs={'required': True, 'class':
                                                   'form-control'}),
            'subject': forms.TextInput(attrs={'required': True, 'class':
                                              'form-control'}),
            'from_email': forms.EmailInput(attrs={'required': True, 'class':
                                                  'form-control'}),
            'message': forms.Textarea(attrs={'required': True, 'class': 'form-control'})

        }
