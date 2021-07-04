#pytube package
from pytube import YouTube
#rich package for terminal
from rich.console import Console
from rich.progress import Progress
# time
import time

console = Console()

#Custom header

console.print("""
███████╗██████╗ ███████╗██████╗ ███████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══███╔╝
███████╗██████╔╝█████╗  ██████╔╝  ███╔╝ 
╚════██║██╔═══╝ ██╔══╝  ██╔══██╗ ███╔╝  
███████║██║     ███████╗██║  ██║███████╗
╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝
""",
              style="dark_cyan")
console.print("Welcome!", style="dark_cyan")
console.print("Made by sperz 2021.", style="dark_cyan")

# Declarated path
path = '/home/sperz/Downloads'

# Start Downloads
try:
    with open('links.txt', 'r') as read:
        for line in read:
            with Progress() as progress:
                console.print(line, style="bold red\n")
                task1 = progress.add_task("[red]Downloading...", total=1000)
                #search link on youtube
                yt = YouTube(line)
                # search only audio
                video = yt.streams.filter(only_audio=True).first()
                #download audio to path
                video.download(path)

                # custom progess bar
                while not progress.finished:
                    progress.update(task1, advance=0.9)
                    time.sleep(0.02)
except KeyboardInterrupt:
    console.print("Ups! some error with Keyboard.", style="bold red")

read.close()

console.print("Finish, Back soon :)!", style="dark_cyan")
