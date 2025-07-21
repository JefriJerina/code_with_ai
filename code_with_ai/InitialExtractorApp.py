# InitialExtractorApp.py

import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import os

import gradio as gr
import speech_recognition as sr

# Function to extract initials
def extract_initials(audio):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)

    try:
        name = recognizer.recognize_google(audio_data)
        initials = ''.join([word[0].upper() + '.' for word in name.split()])
        return f"Detected Name: {name}\nYour Initials: {initials}"
    except sr.UnknownValueError:
        return "Sorry, could not understand the audio."
    except sr.RequestError:
        return "Speech recognition service error."

# Gradio interface (updated)
gr.Interface(
    fn=extract_initials,
    inputs=gr.Audio(type="filepath", label="🎤 Speak Your Full Name"),
    outputs="text",
    title="🧠 Voice to Initials Extractor",
    description="Record your name, and this app will extract your initials."
).launch()


# Initial Extractor using Self RAG
class InitialExtractor:
    def __init__(self):
        self.instructions = "Pick the first letter of each word in the name, capitalize it, and add dots."

    def get_logic(self):
        return self.instructions

    def extract_initials(self, name):
        if not name.strip():
            return "Please enter a valid name."
        words = name.strip().split()
        initials = [word[0].upper() + '.' for word in words]
        return ''.join(initials)

# Streamlit UI
st.set_page_config(page_title="Initial Extractor with Voice", page_icon="🎙️")
st.title("🎙️ Voice-based Initial Extractor")
st.write("Speak or type your full name to get your initials.")

extractor = InitialExtractor()

# Text Input
name_input = st.text_input("Type your Full Name")

# Voice Input
uploaded_audio = st.file_uploader("Or upload a voice recording (.wav or .mp3)", type=["wav", "mp3"])

# Process Voice Input
if uploaded_audio is not None:
    audio_path = "temp_audio.wav"
    if uploaded_audio.name.endswith(".mp3"):
        audio = AudioSegment.from_mp3(uploaded_audio)
        audio.export(audio_path, format="wav")
    else:
        audio = AudioSegment.from_wav(uploaded_audio)
        audio.export(audio_path, format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            spoken_text = recognizer.recognize_google(audio_data)
            st.success(f"Detected Name: {spoken_text}")
            name_input = spoken_text
        except sr.UnknownValueError:
            st.error("Sorry, couldn't understand the audio.")
        except sr.RequestError:
            st.error("Speech recognition service failed.")

    os.remove(audio_path)

# Extract Initials
if st.button("Extract Initials"):
    result = extractor.extract_initials(name_input)
    st.success(f"Your Initials: {result}")

    with st.expander("See how it works (Self RAG Logic)"):
        st.code(extractor.get_logic())
