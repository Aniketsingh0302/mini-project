import time
import pyttsx3
from windows_toasts import Toast, WindowsToaster

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set a voice (change index to switch voices)
engine.setProperty('voice', voices[0].id)  # Use voices[1].id for a different voice

# Set speech rate
engine.setProperty('rate', 150)  # Default is around 200, lower is slower

# Set volume (0.0 to 1.0)
engine.setProperty('volume', 0.9)
APP_ID = "Break Reminder"
toaster = WindowsToaster(APP_ID)
while True:    
    text = "Time to take Break Aniket Relax!!!"
    engine.say(text)
    engine.runAndWait()


    toaster = WindowsToaster('Python App')
    new_toast = Toast()
    new_toast.text_fields = ['Time to take Break Aniket Relax!', 'This is a notification from Python.']
    new_toast.on_activated = lambda _: print('Toast clicked!')
    toaster.show_toast(new_toast)
    time.sleep(2500)
