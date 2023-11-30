# STEPS TO FOLLOW
-- create project 

```python
pip install django

pip install SpeechRecognition

pip install pyttsx3

pip install gtts

pip install pyaudio

django-admin startproject EncryptDecrypt .

python manage.py startapp EncrypterDecrypter

```
# Go to EncryptDecrypt/Settings.py 
-- add ``` 'DIRS': [BASE_DIR / 'EncrypterDecrypter/templates'], ``` in Templates Array
-- add ```  'EncrypterDecrypter', ``` to installed_Apps Array



python manage.py runserver



```


