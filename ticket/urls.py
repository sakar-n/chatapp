from django.urls import path
from .views import Ticket, AddPriority, DeletePriority, PriorityUpdate, DisplayingTickets, Message, DeleteTicket, OpenTicket, CloseTicket, TicketDetail, GetMessage, Test, DisplayingReceivedTickets, DisplayingIssuedTickets, OpenTicketByAdmin, CloseTicketByAdmin, DeleteTicketByAdmin


urlpatterns=[
    path('',Ticket.as_view(), name='ticket'),
    path('test/<int:ticket_id>', Test.as_view(), name='test'),
    path('ticketpriorities/', AddPriority.as_view(), name='ticket_management'),
    path('priority/delete/<int:priority_id>/', DeletePriority.as_view(), name='delete_priority'),
    path('priority/update/<int:priority_id>/', PriorityUpdate.as_view(), name='update_priority'),
    path('mytickets/', DisplayingTickets.as_view(), name='my_tickets'),
    path('openticket/<int:ticket_id>', OpenTicket.as_view(), name='open_ticket'),
    path('closeticket/<int:ticket_id>', CloseTicket.as_view(), name='close_ticket'),
    path('message/<int:ticket_id>/', Message.as_view(), name='message'),
    path('getmessage/<int:ticket_id>/', GetMessage.as_view(), name='getmessage'),
    path('deleteticket/<int:ticket_id>', DeleteTicket.as_view(), name='delete_ticket'),
    path('ticket_view/<int:ticket_id>', TicketDetail.as_view(), name='view_ticket'),
    path('received_tickets/', DisplayingReceivedTickets.as_view(), name='received_tickets'),
    path('issued_tickets/', DisplayingIssuedTickets.as_view(), name='issued_tickets'),
    path('opentickets/<int:ticket_id>', OpenTicketByAdmin.as_view(), name='open_tickets'),
    path('closetickets/<int:ticket_id>', CloseTicketByAdmin.as_view(), name='close_tickets'),
    path('deletetickets/<int:ticket_id>', DeleteTicketByAdmin.as_view(), name='delete_tickets'),
]

