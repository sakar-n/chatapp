from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import TicketForm, AttachmentForm, AddPrioritiesForm
from company.models import Companies, CompanyUser
from .models import Priorities

# Create your views here.
class Ticket(View):
    template_name = 'issuetickets.html'
    ticketform = TicketForm
    attachmentform = AttachmentForm
    
    def get(self, request):
        company_id = CompanyUser.objects.get(user_id=request.user.id).company_id
        priorities = Priorities.objects.filter(company_id=company_id)
        form1 = self.ticketform(company_id=company_id)  # Pass the company_id to the form
        return render(request, self.template_name, {"form1": form1, 'form2': self.attachmentform, "priorities": priorities})
    
    def post(self, request):
        form1 = self.ticketform(request.POST)  # Pass the company_id to the form
        form2 = self.ticketform(request.POST)
        if form1.is_valid:
            form1.save()
        if form2.is_valid:
            form2.save()
            messages.success(request, 'Tickets Issue Successfully')
            return redirect('tickets')
        else:
            messages.success(request, 'Invalid Input, Tickets Cannot be Issued')
            return render(request, self.template_name, {"form1": form1, 'form2': form2})
        
    
class AddPriority(View):
    template_name = "tickets.html"
    priority_form = AddPrioritiesForm
    def get(self, request):
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        priority = Priorities.objects.filter(company_id=company_id, )
        return render(request, self.template_name, {'form':self.priority_form, "priorities":priority })
    
    def post(self, request):
        form = self.priority_form(request.POST)
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        if form.is_valid():
            unsaveform = form.save(commit=False)
            priorityname = form.cleaned_data['priority_name']
            if Priorities.objects.filter(company_id=company_id, priority_name = priorityname).exists():
                messages.error(request, "This Priority level already exist in your system")
                return redirect('ticket_management')
            else:
                unsaveform.company_id = company_id
                unsaveform.save()
                messages.success(request, "Ticket Priorities Added Successfully")
                return redirect('ticket_management')
        else:
            messages.error(request, "Tickets Can't be added")
            return render(request, self.template_name, {'form':form})
        
class DeletePriority(View):
    def get(self, request, priority_id):
        priority = Priorities.objects.get(priority_id=priority_id)
        priority.delete()
        messages.success(request, "Priority Deleted Successfully")
        return redirect('ticket_management')

class PriorityAPI(View):
    def get(self, request):
        copmany_id = CompanyUser.objects.get(copmany_id=request.user.id)
        return redirect('ticket')