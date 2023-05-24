from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import TicketForm, AttachmentForm, AddPrioritiesForm, MessageForm, MessageAttachmentForm
from company.models import Companies, CompanyUser, ForeignUser, ProjectUser
from .models import Priorities, Project, Tickets, MessageModel, MessageAttachments

# Create your views here.
class Ticket(View):
    template_name = 'issuetickets.html'
    ticketform = TicketForm
    attachmentform = AttachmentForm
    def get(self, request):
        company_id = CompanyUser.objects.get(user_id=request.user.id).company_id
        priorities = Priorities.objects.filter(company_id=company_id)
        form1 = self.ticketform(company_id=company_id, request=request)  # Pass the company_id to the form
        return render(request, self.template_name, {"form1": form1, 'form2': self.attachmentform, "priorities": priorities})
    
    def post(self, request):
            company_id = CompanyUser.objects.get(user_id=request.user.id).company_id
            # request.POST['prj']=ForeignUser.objects.filter(id=request.POST['prj'])
            form1 = self.ticketform(request.POST, company_id=company_id, request=request)
            form2 = self.attachmentform(request.POST, request.FILES)
            if form1.is_valid():
                ticket = form1.save(commit=False)
                ticket.issued_by_id = request.user.id
                ticket.priority_id = request.POST['priority_name']
                ticket.prj_id = request.POST['prj']
                ticket.save()
                attachment = form2.save(commit=False)
                attachment.ticket_id = ticket.ticket_id
                print(attachment)
                attachment.save()
                
                messages.success(request, 'Ticket issued successfully')
                return redirect('ticket')
            else:
                messages.error(request, form1.errors)
                return render(request, self.template_name, {"form1": form1, "form2": form2})
       
        
    
class AddPriority(View):
    template_name = "tickets.html"
    priority_form = AddPrioritiesForm
    def get(self, request):
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        priority = Priorities.objects.filter(company_id=company_id )
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

class PriorityUpdate(View):
    template_name = 'priority_update.html'
    updateform = AddPrioritiesForm
    def get(self, request, priority_id):
        priority = get_object_or_404(Priorities, priority_id=priority_id) 
        form_data={
            'priority_name':priority.priority_name
        }
        form = self.updateform(initial=form_data)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, priority_id):
        priority = get_object_or_404(Priorities, priority_id=priority_id)
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        form = self.updateform(request.POST, instance=priority)
        if form.is_valid():
            unsaveform = form.save(commit=False)
            priorityname = form.cleaned_data['priority_name']
            if Priorities.objects.filter(company_id=company_id, priority_name = priorityname).exists():
                messages.error(request, "This Priority level already exist in your system")
                return render(request, self.template_name, {'form':form})
            else:
                unsaveform.save()
                messages.success(request, "Priority Updated Successfully")
                return redirect('/ticket/ticketpriorities/')
        else:
           return render(request, self.template_name, {'form':form})

class DisplayingTickets(View):
    template_name = 'my_tickets.html'
    def get(self, request):
        user_project_id =  ProjectUser.objects.get(user_id = request.user.id).project_id
        displaying_tickets = Tickets.objects.filter(prj_id=user_project_id)
        return render(request, self.template_name, {'displaying_tickets':displaying_tickets })

class Message(View):
    template_name = 'message.html'
    message_form = MessageForm
    attachment = MessageAttachmentForm
    def get(self, request, ticket_id):
        user_project_id =  ProjectUser.objects.get(user_id = request.user.id).project_id
        displaying_tickets = Tickets.objects.filter(prj_id=user_project_id, ticket_id = ticket_id)
        displaying_message = MessageModel.objects.filter(ticket_id = ticket_id)
        displaying_attachment = MessageAttachments.objects.filter(ticket_id = ticket_id)
        return render(request, self.template_name, {'displaying_tickets':displaying_tickets, 'displaying_message':displaying_message, 'displaying_attachment':displaying_attachment, 'form1':self.message_form, 'form2':self.attachment })
    
    def post(self, request, ticket_id):
        user_project_id =  ProjectUser.objects.get(user_id = request.user.id).project_id
        displaying_tickets = Tickets.objects.filter(prj_id=user_project_id, ticket_id = ticket_id)
        displaying_message = MessageModel.objects.filter(ticket_id = ticket_id)
        form1 = self.message_form(request.POST)
        form2 = self.attachment(request.POST, request.FILES)
        if form1.is_valid():
            unsavedform1 = form1.save(commit=False)
            unsavedform1.user_id = request.user.id
            unsavedform1.ticket_id = ticket_id
            unsavedform1.save()
            if form2.is_valid():
                unsavedform2 = form2.save(commit=False)
                unsavedform2.ticket_id = ticket_id
                unsavedform2.message_id = unsavedform1.message_id
                unsavedform2.save()
            messages.success(request, 'message send successfully')
            return redirect('message', ticket_id)
        else:
            messages.error('Invalid Message')
        return render(request, self.template_name, {'displaying_tickets':displaying_tickets, 'displaying_message':displaying_message, 'form1':self.message_form, 'form2':self.attachment })
        
        
class DeleteTicket(View):
    def get(self, request, ticket_id):
        tickets = Tickets.objects.filter(issued_by_id=request.user.id, ticket_id = ticket_id)
        tickets.delete()
        messages.success(request, "Ticekt Deleted Successfully")
        return redirect('index')