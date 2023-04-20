from django import forms
from .models import Companies


        
class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'NITV PVT. LTD', 'class':'form-control'}))
    
    class  Meta:
        model = Companies 
        fields= ['company_name']
    
