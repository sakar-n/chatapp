from django.urls import path
from .views import Ticket, AddPriority, DeletePriority, PriorityUpdate, DisplayingTickets

urlpatterns=[
    path('',Ticket.as_view(), name='ticket'),
    path('ticketpriorities/', AddPriority.as_view(), name='ticket_management'),
    path('priority/delete/<int:priority_id>/', DeletePriority.as_view(), name='delete_priority'),
    path('priority/update/<int:priority_id>/', PriorityUpdate.as_view(), name='update_priority'),
    path('mytickets/', DisplayingTickets.as_view(), name='my_tickets'),
]