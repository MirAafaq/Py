# EncrypterDecrypter/views.py
from django.shortcuts import render
from django.http import HttpResponse
import speech_recognition as sr
import pyttsx3
import tkinter as tk
import threading
from gtts import gTTS
import os
from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import speech_recognition as sr
recognizer = sr.Recognizer()


def stt_action(request):
    if request.method == 'POST':
        try:
            with sr.Microphone() as source:
                print("Speak something...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)  # Adjust timeout as needed

            text = recognizer.recognize_google(audio)
            return JsonResponse({'stt_success': True, 'stt_text': text})
        except sr.UnknownValueError:
            return JsonResponse({'stt_success': False, 'stt_text': 'Could not understand audio'})
        except sr.RequestError as e:
            return JsonResponse({'stt_success': False, 'stt_text': f"Could not request results from Google Speech Recognition service: {e}"})
    else:
        return HttpResponse("Invalid request method")


def index(request):
    return render(request, 'EncrypterDecrypter/index.html')





def encrypt_action(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        key = int(request.POST.get('key', 3))
        ciphertext = encrypt(text, key)
        return render(request, 'EncrypterDecrypter/index.html', {'ciphertext': ciphertext})
    else:
        return HttpResponse("Invalid request method")


def decrypt_action(request):
    if request.method == 'POST':
        ciphertext = request.POST.get('ciphertext')
        key = int(request.POST.get('key', 3))
        plaintext = decrypt(ciphertext, key)
        return render(request, 'EncrypterDecrypter/index.html', {'plaintext': plaintext})
    else:
        return HttpResponse("Invalid request method")


def stt_action(request):
    # Your speech-to-text logic here
    return HttpResponse("Speech-to-text action performed")


def tts_thread(text):
    engine.say(text)
    engine.runAndWait()


def tts_action(request):
    if request.method == 'POST':
        text = request.POST.get('text')

        # Create a gTTS object
        tts = gTTS(text=text, lang='en')

        # Save the generated speech to a file
        tts.save("audio_output.mp3")

        # Play the saved audio file
        os.system("start audio_output.mp3")

        return render(request, 'EncrypterDecrypter/index.html', {'tts_success': True})
    else:
        return HttpResponse("Invalid request method")


def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) + key)
    return encrypted_text


def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        decrypted_text += chr(ord(char) - key)
    return decrypted_text


# Initialize STT recognizer
recognizer = sr.Recognizer()

# Initialize TTS engine
engine = pyttsx3.init()
