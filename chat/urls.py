from django.urls import path
from .views import signup_view, CustomLoginView, CustomLogoutView, chat_view, room_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('chat/', chat_view, name='chat_view'), 
    path('chat/<str:room_name>/', room_view, name='room'),
]
