from django.shortcuts import render
from django.views import View
from .forms import TicketForm, AttachmentForm

# Create your views here.
class Ticket(View):
    template_name = 'issuetickets.html'
    form1 = TicketForm
    form2 = AttachmentForm
    def get(self, request):
        return render(request, self.template_name, {"form1":self.form1, 'form2':self.form2})
        