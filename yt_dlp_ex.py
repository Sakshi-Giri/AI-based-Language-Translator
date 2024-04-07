import yt_dlp
import os

def download_youtube_video():
    try:
        # Accept YouTube video URL from the user
        video_url = input("Enter the YouTube video URL: ")

        # Initialize the yt-dlp downloader
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',  # Output template for the filename
        }
        ydl = yt_dlp.YoutubeDL(ydl_opts)

        # Download the video
        info_dict = ydl.extract_info(video_url, download=True)
        
        # Get the first word of the video title
        title_words = info_dict['title'].split()
        first_word = title_words[0]

        # Construct the new filename
        new_filename = f"{first_word}_{info_dict['id']}.{info_dict['ext']}"

        # Rename the downloaded file
        old_filepath = os.path.join(os.getcwd(), f"{info_dict['title']}.{info_dict['ext']}")
        new_filepath = os.path.join(os.getcwd(), new_filename)
        os.rename(old_filepath, new_filepath)

        print(f"Video downloaded successfully! Saved as: {new_filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
