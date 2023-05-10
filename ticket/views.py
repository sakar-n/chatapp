from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import TicketForm, AttachmentForm, PrioritiesForm
from company.models import Companies

# Create your views here.
class Ticket(View):
    template_name = 'issuetickets.html'
    form1 = TicketForm
    form2 = AttachmentForm
    def get(self, request):
        return render(request, self.template_name, {"form1":self.form1, 'form2':self.form2})
    
class AddPriority(View):
    template_name = "tickets.html"
    priority_form = PrioritiesForm
    def get(self, request):
        return render(request, self.template_name, {'form':self.priority_form })
    
    def post(self, request):
        form = self.priority_form(request.POST)
        company_id = Companies.objects.get(company_id=company_id)
        print(company_id)
        if form.is_valid():
            form.save()
            messages.success(request, "Ticket Priorities Added Successfully")
            return render(request, self.template_name, {'form':form})
        else:
            messages.success(request, "Tickets Can't be added")
            return render(request, self.template_name, {'form':form})