import youtube_dl

def download_youtube_video():
    try:
        video_url = input("Enter the YouTube video URL: ")

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'C:/Users/Sakshi/OneDrive/Documents/sample/%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
