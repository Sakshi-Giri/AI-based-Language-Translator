import os
from assemblyai import Client as AssemblyAI_Client
from langdetect import detect
from gtts import gTTS

# Function to convert audio to text using AssemblyAI
def audio_to_text(audio_file_path, api_key):
    client = AssemblyAI_Client(api_key)
    try:
        transcript = client.transcribe_file(audio_file_path)
        return transcript.text
    except Exception as e:
        print("Error converting audio to text:", e)
        return None

# Function to detect the language of the text
def detect_language(text):
    try:
        language = detect(text)
        return language
    except Exception as e:
        print("Error detecting language:", e)
        return None

# Function to convert text to audio using gTTS
def text_to_audio(text, language, output_file_path):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save(output_file_path)
    except Exception as e:
        print("Error converting text to audio:", e)

# Main function
def main():
    # Prompt the user for the path of the text file
    text_file_path = input("Enter the path of the text file: ")

    # Read the contents of the text file
    try:
        with open(text_file_path, "r", encoding="utf-8") as file:
            text = file.read()
    except Exception as e:
        print("Error reading text file:", e)
        return

    # API key for AssemblyAI (replace with your own)
    assemblyai_api_key = "9ffd005de5384a08b1fa40d71d14c9c1"

    # Convert text to audio
    language = detect_language(text)
    if language is None:
        return
    output_file_path = "output_audio.mp3"
    text_to_audio(text, language, output_file_path)

    print("Audio conversion complete.")

if __name__ == "__main__":
    main()
