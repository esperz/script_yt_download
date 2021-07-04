#pytube package
from pytube import YouTube
#rich package for terminal
from rich.console import Console
from rich.progress import Progress
from rich.prompt import Prompt
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

# declarated path
path = '/home/sperz/Downloads'

# start download

try:
    link = Prompt.ask("Enter the link of YouTube video",
                      default="eg. https://www.youtube.com/watch?...")
    with Progress() as progress:
        console.print(link)
        task1 = progress.add_task("[red]Downloading...", total=1000)
        yt = YouTube(link)
        video = yt.streams.filter(only_audio=True).first()
        video.download(path)

        while not progress.finished:
            progress.update(task1, advance=0.9)
            time.sleep(0.02)
except KeyboardInterrupt:
    console.print("Ups! some error with Keyboard.", style="bold red")

console.print("Finish, Back soon :)!", style="dark_cyan")
