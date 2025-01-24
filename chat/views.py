from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

@login_required
def chat_view(request):
    return render(request, 'chat/chat.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid. Saving user...")
            user = form.save()
            login(request, user)
            print(f"Redirecting to chat_view for user: {user.username}")
            return redirect('chat_view')
        else:
            print("Form is invalid:", form.errors)
    else:
        form = SignUpForm()
    return render(request, 'chat/signup.html', {'form': form})
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    return redirect('/login/')

from .models import Message

def room_view(request, room_name):
    messages = Message.objects.filter(room_name=room_name).order_by('timestamp')
    print(messages)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
        'users': users
    })
from .models import ChatRoom

def home_view(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/home.html', {'rooms': rooms})

from django.shortcuts import redirect

def create_room(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        ChatRoom.objects.create(name=room_name)
        return redirect('/')


from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'chat/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect to login after logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class ChatRoomView(LoginRequiredMixin, TemplateView):
    # Chatroom view logic
    template_name = 'chat/room.html'
from django.contrib.auth.decorators import login_required

@login_required
def room_view(request, room_name):
    messages = Message.objects.filter(room_name=room_name, deleted=False).order_by('timestamp')
    users = User.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
        'users': users
    })
