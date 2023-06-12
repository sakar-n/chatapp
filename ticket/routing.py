from django.urls import  path
from .consumers import TicketConsumer

websocket_urlpatterns =[
    path('hello/', TicketConsumer.as_asgi()),
]