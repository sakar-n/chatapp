from django import forms
from .models import Tickets, Attachments

class TicketForm(forms.ModelForm):
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'subject', 'class':'form-controller'}))
    message = forms.CharField(max_length=384000, required=True, widget=forms.Textarea(attrs={'placeholder':'message', 'class':'form-controller'}))
    
    class Meta:
        model = Tickets
        fields =['subject','message']
        
class AttachmentForm(forms.ModelForm):
    attachment = forms.FileField()
    
    class Meta:
        model = Attachments
        fields =['attachment']
    