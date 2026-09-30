import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
import pyttsx3
import os
import pygame
from gtts import gTTS
import speech_recognition as sr

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()
available_voices = engine.getProperty('voices')

# Language mapping for TTS
language_map = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml"
}

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = "".join(page.extract_text() + "\n" for page in reader.pages if page.extract_text())
        return text.strip() if text else "No text found in PDF."
    except Exception as e:
        return f"Error reading PDF: {e}"

# Convert text to speech (used for both PDF & manual input)
def convert_text_to_audio(text):
    if not text:
        result_label.config(text="No text to convert!", fg="red")
        return

    audio_ext = "mp3" if language_var.get() in ["Telugu", "Tamil", "Kannada", "Malayalam"] else "wav"
    audio_path = filedialog.asksaveasfilename(defaultextension=f".{audio_ext}", filetypes=[("Audio files", f"*.{audio_ext}")])

    if not audio_path:
        result_label.config(text="Audio path not selected!", fg="red")
        return

    try:
        if language_var.get() in ["Telugu", "Tamil", "Kannada", "Malayalam"]:
            tts = gTTS(text=text, lang=language_map[language_var.get()])
            tts.save(audio_path)
        else:
            engine.save_to_file(text, audio_path)
            engine.runAndWait()

        result_label.config(text=f"Audio saved as {audio_path}", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

# Play audio without background music
def play_audio_without_music():
    speech_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if not speech_path or not os.path.exists(speech_path):
        result_label.config(text="Error: Speech audio file not found!", fg="red")
        return

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(speech_path)
        pygame.mixer.music.play()
        result_label.config(text="Playing speech audio...", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

# Play audio with background music
def play_audio_with_music():
    speech_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3")])
    if not speech_path or not os.path.exists(speech_path):
        result_label.config(text="Error: Speech audio file not found!", fg="red")
        return

    music_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if not music_path or not os.path.exists(music_path):
        result_label.config(text="Error: Background music file not found!", fg="red")
        return

    try:
        pygame.mixer.init()
        speech = pygame.mixer.Sound(speech_path)
        speech.set_volume(1.0)

        pygame.mixer.music.load(music_path)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        speech.play()
        result_label.config(text="Playing speech with background music...", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

# Stop all audio
def stop_audio():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    result_label.config(text="Audio stopped.", fg="blue")

# Open PDF and extract text
def open_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        text = extract_text_from_pdf(file_path)
        pdf_text_box.delete("1.0", tk.END)
        pdf_text_box.insert(tk.END, text)

# Convert PDF text to audio
def convert_pdf_to_audio():
    text = pdf_text_box.get("1.0", tk.END).strip()
    convert_text_to_audio(text)

# Convert manual input text to audio
def convert_manual_text_to_audio():
    text = manual_text_box.get("1.0", tk.END).strip()
    convert_text_to_audio(text)

# Speech-to-text function
def record_and_convert_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        result_label.config(text="Listening... Speak now!", fg="blue")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        manual_text_box.delete("1.0", tk.END)
        manual_text_box.insert(tk.END, text)
        result_label.config(text="Speech converted to text successfully!", fg="green")
    except sr.UnknownValueError:
        result_label.config(text="Could not understand the audio.", fg="red")
    except sr.RequestError:
        result_label.config(text="Error connecting to Google API.", fg="red")

# GUI setup
root = tk.Tk()
root.title("Audio Processing Tool")

# ====== PDF to Speech Section ======
pdf_frame = tk.LabelFrame(root, text="📄 PDF to Speech", padx=10, pady=10)
pdf_frame.pack(padx=10, pady=5, fill="both")

tk.Button(pdf_frame, text="Open PDF", command=open_pdf).pack()
pdf_text_box = tk.Text(pdf_frame, width=50, height=5)
pdf_text_box.pack(pady=5)

language_var = tk.StringVar(value="English")
tk.Label(pdf_frame, text="Select Language:").pack()
tk.OptionMenu(pdf_frame, language_var, *language_map.keys()).pack()

tk.Button(pdf_frame, text="Convert PDF to Audio", command=convert_pdf_to_audio).pack(pady=5)

# ====== Manual Text-to-Speech Section ======
manual_tts_frame = tk.LabelFrame(root, text="🖊️ Manual Text-to-Speech", padx=10, pady=10)
manual_tts_frame.pack(padx=10, pady=5, fill="both")

tk.Label(manual_tts_frame, text="Enter Text Below:").pack()
manual_text_box = tk.Text(manual_tts_frame, width=50, height=5)
manual_text_box.pack(pady=5)

tk.Button(manual_tts_frame, text="Convert Text to Audio", command=convert_manual_text_to_audio).pack(pady=5)

# ====== Play Audio Section ======
audio_frame = tk.LabelFrame(root, text="🔊 Play Audio", padx=10, pady=10)
audio_frame.pack(padx=10, pady=5, fill="both")

tk.Button(audio_frame, text="Play Audio Without Background Music", command=play_audio_without_music).pack(pady=5)
tk.Button(audio_frame, text="Play Audio With Background Music", command=play_audio_with_music).pack(pady=5)
tk.Button(audio_frame, text="Stop Audio", command=stop_audio).pack(pady=5)

# ====== Speech-to-Text Section ======
stt_frame = tk.LabelFrame(root, text="🎤 Speech-to-Text", padx=10, pady=10)
stt_frame.pack(padx=10, pady=5, fill="both")

tk.Button(stt_frame, text="Record & Convert to Text", command=record_and_convert_audio).pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=5)

root.mainloop()
