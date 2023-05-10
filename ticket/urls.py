from django.urls import path
from .views import Ticket, AddPriority

urlpatterns=[
    path('ticket/',Ticket.as_view(), name='ticket'),
    path('ticketpriorities/', AddPriority.as_view(), name='ticket_management'),
]