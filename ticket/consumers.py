import json
from channels.generic.websocket import WebsocketConsumer
from .models import MessageModel
from django.core.serializers import serialize
from channels.db import database_async_to_sync

class TicketConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send_initial_data()  # Send initial data on connection

    def send_initial_data(self):
        messages = MessageModel.objects.all()
        messagelist = serialize('json', messages)
        self.send(json.dumps({'message': messagelist}))
    
