from pytube import YouTube
def download_video(url):
    YouTube(url).streams.first().download()
    video_yt = YouTube(url)
    video_yt = video_yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    try:
        video_yt.download()
    except ValueError:
        print("there was an error downloading your youtube video")
    print("Successful")
url = input("Input your youtube URL: \n")
download_video(url)
