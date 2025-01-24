import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']

        # Save the message to the database
        Message.objects.create(
            sender=user,
            room_name=self.room_name,
            content=message
        )

        # Broadcast the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'{user.username}: {message}'
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send the message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    async def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json.get('message')
    typing = text_data_json.get('typing', False)

    if typing:
        # Notify others that the user is typing
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_typing',
                'user': self.scope['user'].username,
                'typing': typing,
            }
        )
    elif message:
        # Save and broadcast the message
        Message.objects.create(sender=self.scope['user'], room_name=self.room_name, content=message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'{self.scope["user"].username}: {message}'
            }
        )

async def user_typing(self, event):
    user = event['user']
    typing = event['typing']
    await self.send(text_data=json.dumps({
        'typing': typing,
        'user': user
    }))
