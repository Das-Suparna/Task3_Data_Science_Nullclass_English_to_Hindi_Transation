import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator
from datetime import datetime
from tkinter import *

def reset_text_areas():
    english_audio_text.delete(1.0, tk.END)
    hindi_translation_text.delete(1.0, tk.END)
    start_of_translation_status.config(text="Please Press 'Translate' to start")

def translate_english_audio_to_hindi():  
    reset_text_areas()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        start_of_translation_status.config(text="Listening...")

        try:
            audio = r.listen(source, timeout=5)
            start_of_translation_status.config(text="Processing...")

            text = r.recognize_google(audio)
            language = detect_language(text)
            if language == 'en':
                
                if text.strip().lower().startswith(('m', 'o')):
                    start_of_translation_status.config(text="Cannot Translate as starts with 'm' or 'o'.")
                else:
                    english_audio_text.insert(tk.END, text)  # Display English audio text
                    translation_into_hindi = hindi_text_translate_from_english_audio(text)
                    hindi_translation_text.insert(tk.END, translation_into_hindi)  # Display Hindi translation
            else:
                start_of_translation_status.config(text="Only English audio is allowed.")
        except sr.UnknownValueError:
            start_of_translation_status.config(text="Sorry, I couldn't understand. Please try again.")
        except sr.RequestError:
            start_of_translation_status.config(text="Failed to connect to Google Speech Recognition service.")

def hindi_text_translate_from_english_audio(audio_text):
    translator = Translator()
    translation_into_hindi = translator.translate(audio_text, dest='hi')
    return translation_into_hindi.text

def detect_language(text):
    translator = Translator()
    detected_language = translator.detect(text)
    return detected_language.lang

def main():
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time >= "18:00:00":
        translate_english_audio_to_hindi()
    else:
        start_of_translation_status.config(text="Please try after 6 PM IST")

# Tkinter setup
task3_tkinter_window = tk.Tk()
task3_tkinter_window.title("Converting an English Audio into a Hindi Translation")
task3_tkinter_window.geometry("600x600+460+100")
task3_tkinter_window.configure(background="#ffffff")

# GUI elements
frame = Frame(task3_tkinter_window, background="White", highlightbackground="black", highlightthickness=2, bd=0)
frame.place(x=50,y=70,width=500,height=430)

start_of_translation_status = Label(frame, text="Please Press 'Translate' to start", bg="White", font=('Verdana', 14))
start_of_translation_status.place(x=0,y=4,width=489,height=70)

translate_button = Button(frame, text="Translate", command=main, bg="Blue",fg="white",font = ('arial', 13, 'bold'))
translate_button.place(x=200,y=80,width=100,height=30)

# Adding labels to display English audio and its translation
english_audio_label = Label(frame, text="English Audio:", bg="White", font=('Verdana', 13, 'bold'))
english_audio_label.place(x=10, y=120)

# Adding text boxes to display English audio and its translation
english_audio_text = Text(frame, wrap=WORD, height=3, width=53 ,font = ('arial', 13, 'bold'))
english_audio_text.place(x=10, y=160)

hindi_translation_label = Label(frame, text="Hindi Translation:", bg="White", font=('Verdana', 13, 'bold'))
hindi_translation_label.place(x=10, y=230)

hindi_translation_text = Text(frame, wrap=WORD, height=3, width=53 ,font = ('arial', 13, 'bold'))
hindi_translation_text.place(x=10, y=270)

# Creating a custom style for the Quit button with blue background and white foreground
quit_button = Button(frame, text="Close", command=task3_tkinter_window.quit, bg="Red",fg="white",font = ('arial', 13, 'bold'))
quit_button.place(x=220,y=350,width=50,height=30)

# Run the Tkinter event loop
task3_tkinter_window.mainloop()