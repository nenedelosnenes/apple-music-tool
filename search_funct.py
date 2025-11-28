from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.contrib.search import Search, Filter
# url = "https://www.youtube.com/watch?v=Z4ZoZB-dHtg&list=RDZ4ZoZB-dHtg&start_radio=1&pp=ygUXYXl1ZGFtZSBpbWFnaW5hciBzcGVlZHmgBwE%3D"

# filters = (
   # Filter.create()
    #    .type(Filter.Type.AUDIO)
# )

#uses just text to search for videos
s = Search('ayudame imaginar sir speedy')
for video in s.videos:
    print(video.watch_url)

#downloads the mp3 file to the specified folder
def download_funct():
    yt = YouTube(video.watch_url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    ys.download()



download_funct()
