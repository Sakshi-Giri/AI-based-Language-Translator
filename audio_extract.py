from moviepy.editor import * # type: ignore
import os

# Function to extract audio from video
def extract_audio(video_file_path):
    try:
        # Load the video clip
        clip = VideoFileClip(video_file_path)

        # Extract the audio
        audio_file_name = os.path.splitext(os.path.basename(video_file_path))[0] + "_audio.mp3"
        audio_file_path = os.path.join(os.path.dirname(video_file_path), audio_file_name)
        clip.audio.write_audiofile(audio_file_path)

        print(f"Audio extracted and saved to: {audio_file_path}")
    except Exception as e:
        print("Error extracting audio:", e)

def main():
    # Prompt the user for the path of the video file
    video_file_path = input("Enter the path of the video file: ")

    # Extract audio from video
    extract_audio(video_file_path)

if __name__ == "__main__":
    main()
