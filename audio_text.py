import os
import assemblyai as aai

aai.settings.api_key = "9ffd005de5384a08b1fa40d71d14c9c1"
transcriber = aai.Transcriber()

# Prompt the user to enter the path of the audio file
audio_path = input("Enter the path of the audio file: ")

# Extract the audio file name
audio_file_name = os.path.splitext(os.path.basename(audio_path))[0]

# Transcribe the audio
transcript = transcriber.transcribe(audio_path)

# Write the transcript to a text file
output_text_file = f"{audio_file_name}_text.txt"
with open(output_text_file, "w") as file:
    file.write(transcript.text)

print(transcript.text)
