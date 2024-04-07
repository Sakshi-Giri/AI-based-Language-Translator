from googletrans import Translator
import os

translator = Translator()

# Prompt the user for the path of the text file
file_path = input("Enter the path of the text file: ")

# Extract the directory and file name components
directory, filename = os.path.split(file_path)
filename_without_extension, extension = os.path.splitext(filename)

# Read the contents of the text file
with open(file_path, "r", encoding="utf-8") as file:
    text_to_translate = file.read()

# Prompt the user for the desired language
destination_language = input("Enter the desired language (e.g., 'ja' for Japanese): ")

# Translate the text to the desired language
translated_text = translator.translate(text_to_translate, dest=destination_language)

# Print the translated text
print("Translated text:")
print(translated_text.text)

# Construct the output file path
output_file_path = os.path.join(directory, f"{filename_without_extension}_translated.txt")

# Save the translated text to a text file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(translated_text.text)

print(f"Translated text saved to {output_file_path}")
