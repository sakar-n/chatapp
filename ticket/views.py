from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import TicketForm, AttachmentForm, AddPrioritiesForm, MessageForm, MessageAttachmentForm
from company.models import Companies, CompanyUser, ForeignUser, ProjectUser, Project, AssiciateCompany
from .models import Priorities, Project, Tickets, MessageAttachments, Attachments, Room, Messagemodel, Message
from django.core.serializers import serialize
from django.http import JsonResponse
from project.models import PasariteUser
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@csrf_exempt
@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter()

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


class Ticket(View):
    template_name = 'issuetickets.html'
    ticketform = TicketForm
    attachmentform = AttachmentForm
    def get(self, request):
        try:
            company_id = CompanyUser.objects.get(user_id=request.user.id).company_id
            priorities = Priorities.objects.filter(company_id=company_id)
            form1 = self.ticketform(company_id=company_id, request=request)  # Pass the company_id to the form
            return render(request, self.template_name, {"form1": form1, 'form2': self.attachmentform, "priorities": priorities, "active_link" : "isssueTickets"})
        except:
            company_id = PasariteUser.objects.get(user_id=request.user.id).company_id
            priorities = Priorities.objects.filter(company_id=company_id)
            form1 = self.ticketform(company_id=company_id, request=request)  # Pass the company_id to the form
            return render(request, self.template_name, {"form1": form1, 'form2': self.attachmentform, "priorities": priorities, "active_link" : "isssueTickets"})
        
    def post(self, request):
        try:
            company_id = CompanyUser.objects.get(user_id=request.user.id).company_id
            # request.POST['prj']=ForeignUser.objects.filter(id=request.POST['prj'])
            form1 = self.ticketform(request.POST, company_id=company_id, request=request)
            form2 = self.attachmentform(request.POST, request.FILES)
            if form1.is_valid():
                ticket = form1.save(commit=False)
                ticket.issued_by_id = request.user.id
                ticket.priority_id = request.POST['priority_name']
                ticket.prj_id = request.POST['prj']
                room_slug = slugify(ticket.name)
                room = Room.objects.create(name=ticket.name, slug=room_slug)
                ticket.room = room
                ticket.save()
        
                if form1.is_valid() and 'file' in request.FILES: 
                    attachment = form2.save(commit=False)
                    attachment.ticket_id = ticket.ticket_id
                    attachment.save()
                
                messages.success(request, 'Ticket issued successfully')
                return redirect('ticket')
        except:
            company_id = PasariteUser.objects.get(user_id=request.user.id).company_id
            form1 = self.ticketform(request.POST, company_id=company_id, request=request)
            form2 = self.attachmentform(request.POST, request.FILES)
            if form1.is_valid():
                ticket = form1.save(commit=False)
                ticket.issued_by_id = request.user.id
                ticket.priority_id = request.POST['priority_name']
                project_name = form1.cleaned_data['prj']
                project = Project.objects.filter(project_name=project_name).first() 
                ticket.prj_id = project.project_id

                room_slug = slugify(ticket.subject)
                room = Room.objects.create(name=ticket.name, slug=room_slug)
                ticket.room = room

                ticket.save()

                if form1.is_valid() and 'file' in request.FILES: 
                    attachment = form2.save(commit=False)
                    attachment.ticket_id = ticket.ticket_id
                    attachment.save()
                
                messages.success(request, 'Ticket issued successfully')
                return redirect('ticket')
            else:
                messages.error(request, form1.errors)
                return render(request, self.template_name, {"form1": form1, "form2": form2,  "active_link" : "isssueTickets"})
        
        
    
class AddPriority(View):
    template_name = "tickets.html"
    priority_form = AddPrioritiesForm
    def get(self, request):
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        priority = Priorities.objects.filter(company_id=company_id )
        return render(request, self.template_name, {'form':self.priority_form, "priorities":priority, 'active_link':"ticketPriorities"})
    
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
            messages.error(request, "Tickets Can't be added")
        else:
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
        user_project_id =  ProjectUser.objects.filter(user_id=request.user.id).values_list('project_id', flat=True)
        displaying_tickets = Tickets.objects.filter(prj_id__in=user_project_id).order_by('-created_at')
        attachments = Attachments.objects.filter(ticket_id__in=displaying_tickets)
        return render(request, self.template_name, {'displaying_tickets':displaying_tickets, 'attachments':attachments, "active_link" : "receivedTickets"})

class Messages(View):
    base_template = 'base.html'
    userbase_template = 'userbase.html'
    host_user_base = 'host_user_base.html'
    template_name = 'message.html'
    message_form = MessageForm
    attachment = MessageAttachmentForm
    def get(self, request, ticket_id):
        user_project_id =  ProjectUser.objects.filter(user_id=request.user.id).values_list('project_id', flat=True)
        displaying_tickets = Tickets.objects.filter(prj_id__in=user_project_id, ticket_id=ticket_id)
        ramey = Tickets.objects.get(ticket_id=ticket_id)
        displaying_message = Messagemodel.objects.filter(ticket_id = ticket_id)
        displaying_attachment = MessageAttachments.objects.filter(ticket_id = ticket_id)
        user_id = request.user.id
        if PasariteUser.objects.filter(user_id=user_id).exists():
            return render(request, self.template_name, {'extend_template': self.host_user_base, 'displaying_tickets': displaying_tickets, 'displaying_message': displaying_message, 'displaying_attachment': displaying_attachment, 'ramey': ramey, 'form1': self.message_form, 'form2': self.attachment, "ticket_id": ticket_id, "user_id": user_id})
        elif request.user.first_name:
            return render(request, self.template_name, {'extend_template': self.userbase_template, 'displaying_tickets': displaying_tickets, 'displaying_message': displaying_message, 'displaying_attachment': displaying_attachment, 'ramey': ramey, 'form1': self.message_form, 'form2': self.attachment, "ticket_id": ticket_id, "user_id": user_id})
        else:
            return render(request, self.template_name, {'extend_template': self.base_template, 'displaying_tickets': displaying_tickets, 'displaying_message': displaying_message, 'displaying_attachment': displaying_attachment, 'ramey': ramey, 'form1': self.message_form, 'form2': self.attachment, "ticket_id": ticket_id, "user_id": user_id})
    def post(self, request, ticket_id):
        user_project_id =  ProjectUser.objects.filter(user_id=request.user.id).values_list('project_id', flat=True)
        displaying_tickets = Tickets.objects.filter(prj_id__in=user_project_id, ticket_id=ticket_id)
        displaying_message = Messagemodel.objects.filter(ticket_id = ticket_id)
        displaying_attachment = MessageAttachments.objects.filter(ticket_id = ticket_id)
        form1 = self.message_form(request.POST)
        form2 = self.attachment(request.POST, request.FILES)
        if form1.is_valid():
            unsavedform1 = form1.save(commit=False)
            if not unsavedform1.message and 'file' not in request.FILES:
                messages.error(request, 'Invalid Message: Message cannot be empty')
                return redirect('message', ticket_id)
            unsavedform1.user_id = request.user.id
            unsavedform1.ticket_id = ticket_id
            unsavedform1.save()
            if form2.is_valid() and 'file' in request.FILES:
                unsavedform2 = form2.save(commit=False)
                unsavedform2.ticket_id = ticket_id
                unsavedform2.message_id = unsavedform1.message_id
                unsavedform2.save()
            return redirect('message', ticket_id)
        else:
            messages.error('Invalid Message')
            return render(request, self.template_name, {'displaying_tickets':displaying_tickets, 'displaying_message':displaying_message, 'displaying_attachment':displaying_attachment, 'form1':self.message_form, 'form2':self.attachment })
        


class GetMessage(View):
    template_name = 'message.html'
    message_form = MessageForm
    attachment = MessageAttachmentForm
    def get(self, request, ticket_id):
        user_project_id =  ProjectUser.objects.get(user_id = request.user.id).project_id
        displaying_tickets = Tickets.objects.filter(prj_id=user_project_id, ticket_id = ticket_id)
        displaying_message = Messagemodel.objects.filter(ticket_id = ticket_id)
        displaying_attachment = MessageAttachments.objects.filter(ticket_id = ticket_id)
        # messagelist = serialize('json', displaying_message)
        # print(messagelist)
        return JsonResponse({"messages":list(displaying_message.values()), "displaying_attachment":list(displaying_attachment.values()), "displaying_tickets":list(displaying_tickets.values()) })

    # def post(self, request, ticket_id):
    #     user_project_id =  ProjectUser.objects.get(user_id = request.user.id).project_id
    #     displaying_tickets = Tickets.objects.filter(prj_id=user_project_id, ticket_id = ticket_id)
    #     displaying_message = Messagemodel.objects.filter(ticket_id = ticket_id)
    #     form1 = self.message_form(request.POST)
    #     form2 = self.attachment(request.POST, request.FILES)
    #     if form1.is_valid():
    #         unsavedform1 = form1.save(commit=False)
    #         unsavedform1.user_id = request.user.id
    #         unsavedform1.ticket_id = ticket_id
    #         unsavedform1.save()
    #         if form2.is_valid() and 'file' in request.FILES:
    #             unsavedform2 = form2.save(commit=False)
    #             unsavedform2.ticket_id = ticket_id
    #             unsavedform2.message_id = unsavedform1.message_id
    #             unsavedform2.save()
    #         return redirect('message', ticket_id)
    #     else:
    #         messages.error('Invalid Message')
    #     return render(request, self.template_name, {'displaying_tickets':displaying_tickets, 'displaying_message':displaying_message, 'form1':self.message_form, 'form2':self.attachment })

        
class DeleteTicket(View):
    def get(self, request, ticket_id):
            tickets = Tickets.objects.filter(issued_by_id=request.user.id, ticket_id = ticket_id)
            tickets.delete()
            messages.success(request, "Ticket Deleted Successfully")
            return redirect('index')


class OpenTicket(View):
    def get(self, request, ticket_id):
        user_project_id = ProjectUser.objects.filter(user_id=request.user.id).values_list('project_id', flat=True)
        open_ticket = Tickets.objects.get(prj_id__in=user_project_id, ticket_id=ticket_id)
        open_ticket.status = True
        open_ticket.save()
        messages.success(request, 'Hurray, You have opened the project')
        return redirect('my_tickets')
    
class CloseTicket(View):
    def get(self, request, ticket_id):
        user_project_id = ProjectUser.objects.filter(user_id=request.user.id).values_list('project_id', flat=True)
        open_ticket = Tickets.objects.get(prj_id__in=user_project_id, ticket_id=ticket_id)
        open_ticket.closed_status = True
        open_ticket.save()
        messages.success(request, 'Ticket Closed Successfullly')
        return redirect('my_tickets')

class TicketDetail(View):
    template_name = 'ticket_read.html'
    def get(self, request, ticket_id):
            open_ticket = Tickets.objects.filter(ticket_id=ticket_id)
            attachments = Attachments.objects.filter(ticket_id=ticket_id)
            return render(request, self.template_name, {'open_ticket': open_ticket, 'attachments':attachments})

            
        
def test(request):
    return render(request, 'test.html')

class Test(View):
    message_form = MessageForm
    attachment = MessageAttachmentForm
    def get(self, request, ticket_id):
        user_project_id =  ProjectUser.objects.get(user_id = request.user.id).project_id
        displaying_tickets = Tickets.objects.filter(prj_id=user_project_id, ticket_id = ticket_id)
        displaying_message = Messagemodel.objects.filter(ticket_id = ticket_id)
        displaying_attachment = MessageAttachments.objects.filter(ticket_id = ticket_id)
        return render(request, 'test.html', {'displaying_tickets':displaying_tickets, 'displaying_message':displaying_message, 'form1':self.message_form, 'form2':self.attachment ,"ticket_id":ticket_id})
    

class DisplayingReceivedTickets(View):
    template_name = 'received_ticket.html'
    def get(self, request):
        company_id =  Companies.objects.get(user_id = request.user.id).company_id
        project_id = Project.objects.filter(company_id = company_id)
        displaying_tickets = Tickets.objects.filter(prj_id__in=project_id).order_by('-created_at')
        return render(request, self.template_name, {'displaying_tickets':displaying_tickets, 'active_link':"receivedTickets"})

class DisplayingIssuedTickets(View):
    template_name = 'issued_ticket.html'
    def get(self, request):
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        associate_companies = AssiciateCompany.objects.filter(company_id=company_id)
        projects = [associate_company.project for associate_company in associate_companies]
        displaying_tickets = Tickets.objects.filter(prj_id__in=projects).order_by('status').order_by('closed_status').order_by('-created_at')
        return render(request, self.template_name, {'displaying_tickets': displaying_tickets, 'active_link':"IssuedTickets"})

class OpenTicketByAdmin(View):
    def get(self, request,  ticket_id):
        open_ticket = Tickets.objects.get(ticket_id=ticket_id)
        open_ticket.status = True
        open_ticket.save()
        messages.success(request, 'Hurray, You have opened the project')
        return redirect('received_tickets')

class CloseTicketByAdmin(View):
    def get(self, request,  ticket_id):
        open_ticket = Tickets.objects.get(ticket_id=ticket_id)
        open_ticket.closed_status = True
        open_ticket.save()
        messages.success(request, 'Ticket Closed Successfullly')
        return redirect('received_tickets')

class DeleteTicketByAdmin(View):
     def get(self, request,  ticket_id):
        delete_ticket = Tickets.objects.get(ticket_id=ticket_id)
        delete_ticket.delete()
        messages.success(request, "Ticket Deleted Successfully")
        return redirect('issued_tickets')
    
