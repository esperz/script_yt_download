from pytube import YouTube
from colorama import Fore, init

init(autoreset=True)

path = '/home/sperz/Downloads'

url = [
    'https://www.youtube.com/watch?v=BH6T3CTuncc',
    'https://www.youtube.com/watch?v=Qk5M0LHMchM',
    'https://www.youtube.com/watch?v=zCrsWJSwoi4'
]

for video in url:
    yt = YouTube(video)
    video = yt.streams.filter(only_audio=True).first()
    video.download(path)

print(Fore.GREEN + 'done')