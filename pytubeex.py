from plyer import notification
from pytube import YouTube

def video(link, path):
    yt = YouTube(link)
    vid = yt.streams.get_highest_resolution()
    vid.download(output_path = path)
    notification.ntify(title = "Announcement", message = "your video has finished downloading", timeout = 10)

    if __name__ == "__main__":
        while True:
            linked = input("Enter the link : ")
            pt = input("Enter the path : ")
            video(linked, pt)
            con = input("Continue download ")