from django.urls import path
from .views import Ticket, AddPriority, DeletePriority

urlpatterns=[
    path('ticket/',Ticket.as_view(), name='ticket'),
    path('ticketpriorities/', AddPriority.as_view(), name='ticket_management'),
    path('priority/delete/<int:priority_id>/', DeletePriority.as_view(), name='delete_priority'),  
]