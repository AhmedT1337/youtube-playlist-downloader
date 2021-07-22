import pafy
from pytube import Playlist

url = str(input("playlist link : "))
playlist = Playlist(url)

cqv = pafy.new(playlist[0])

counter = 0

for res in cqv.streams :
    print (f"{counter} : {res}")
    counter += 1

quality = int(input("which stream you like to choose (in index way) ? "))

for item in playlist :
    video = pafy.new(item)
    video.streams[quality].download()
