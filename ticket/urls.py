from django.urls import path
from .views import Ticket, AddPriority, DeletePriority, PriorityUpdate, DisplayingTickets, Message, DeleteTicket, OpenTicket, CloseTicket, TicketDetail

urlpatterns=[
    path('',Ticket.as_view(), name='ticket'),
    path('ticketpriorities/', AddPriority.as_view(), name='ticket_management'),
    path('priority/delete/<int:priority_id>/', DeletePriority.as_view(), name='delete_priority'),
    path('priority/update/<int:priority_id>/', PriorityUpdate.as_view(), name='update_priority'),
    path('mytickets/', DisplayingTickets.as_view(), name='my_tickets'),
    path('openticket/<int:ticket_id>', OpenTicket.as_view(), name='open_ticket'),
    path('closeticket/<int:ticket_id>', CloseTicket.as_view(), name='close_ticket'),
    path('message/<int:ticket_id>/', Message.as_view(), name='message'),
    path('deleteticket/<int:ticket_id>', DeleteTicket.as_view(), name='delete_ticket'),
    path('ticket_view/<int:ticket_id>', TicketDetail.as_view(), name='view_ticket'),
]