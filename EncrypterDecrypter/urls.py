# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('encrypt/', encrypt_action, name='encrypt'),
    path('decrypt/', decrypt_action, name='decrypt'),
    path('tts/', tts_action, name='tts'),
    path('stt/', stt_action, name='stt'),


]
