from .models import ProjectParasite, PasariteUser
from company.models import CompanyUser
from django import forms

class ParasiteForm(forms.Form):
    user_id = forms.ModelChoiceField(queryset=PasariteUser.objects.all())
    
    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('company_id')
        super(ParasiteForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].queryset = PasariteUser.objects.filter(company_id=company_id)
        self.fields['user_id'].label_from_instance = self.get_user_email

    def get_user_email(self, instance):
        return instance.user.email