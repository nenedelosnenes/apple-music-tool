#basic url downloading function 
import os
from pytubefix import YouTube, Search
from pytubefix.cli import on_progress


# makes new folder titled downloaded songs if not created already
directory_name = "Downloaded Songs"

if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print(f"The folder '{directory_name} has been created inside of the program files.")

# finds videos based on search term

s = Search('ayudame imaginar sir speedy')

for video in s.videos:
    print(video.watch_url)
#downloads the mp3 file to the specified folder
def download_funct():
    yt = YouTube(video.watch_url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    ys.download(directory_name)


