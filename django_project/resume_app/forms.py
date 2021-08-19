from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(widget=forms.TextInput(
        attrs={'required': True, 'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'required': True, 'class': 'form-control'}))
    from_email = forms.CharField(widget=forms.EmailInput(
        attrs={'required': True, 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'required': True, 'class': 'form-control'}))
