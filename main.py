from enum import Enum
from types import SimpleNamespace
from rich.console import Console
from rich.table import Table
from rich.text import Text
import pyttsx3 as pyt3
from os import getlogin, name
from pathlib import Path
from subprocess import run
from datetime import datetime

def speak(text):
    console.print(text)
    engine.say(Text.from_markup(text).plain)
    engine.runAndWait()

class Command(Enum):
    HELLO = "hello"
    HELP = "help"
    ECHO = "echo"
    WHOAMI = "whoami"
    DATE = "date"
    TIME = "time"
    DATETIME = "datetime"
    PWD = "pwd"
    CLEAR = "clear"
    EXIT = "exit"

config = SimpleNamespace(
    rate=160,
    volume=0.35
)

console = Console()

engine = pyt3.init()
engine.setProperty("rate", config.rate)
engine.setProperty("volume", config.volume)

speak("[green]Enter help to show commands[/green]")

while True:
    try:
        user_input = console.input("[bold blue]>> [/bold blue]")
        parts = user_input.split(" ", 1)

        command = Command(parts[0])

    except KeyboardInterrupt:
        speak("[yellow]Exit the program..[/yellow]")
        break

    except ValueError:
        speak("[red]Unknown Command![/red]")
        continue

    if command == Command.HELLO:
        speak("[green]Hello, User![/green]")

    elif command == Command.HELP:
        table = Table(title="Commands")

        table.add_column("Command", style="cyan")
        table.add_column("Description", style="white")

        table.add_row("hello", "Say hello")
        table.add_row("echo", "Print text")
        table.add_row("date", "Show current date")
        table.add_row("time", "Show current time")
        table.add_row("datetime", "Show current date and time")
        table.add_row("clear", "Clear terminal")
        table.add_row("help", "Show commands")
        table.add_row("pwd", "Show current directory")
        table.add_row("whoami", "Show current user")
        table.add_row("exit", "Exit the program")

        console.print(table)

    elif command == Command.PWD:
        speak(str(Path.cwd()))

    elif command == Command.WHOAMI:
        speak(getlogin())

    elif command == Command.CLEAR:
        run(["cls" if name == "nt" else "clear"])

    elif command == Command.ECHO:
        if len(parts) > 1:
            speak(parts[1])
        else:
            speak("[red]Nothing to echo[/red]")

    elif command == Command.DATE:
        speak(datetime.now().strftime("%d.%m.%Y"))

    elif command == Command.TIME:
        speak(datetime.now().strftime("%H:%M:%S"))

    elif command == Command.DATETIME:
        speak(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    elif command == Command.EXIT:
        speak("[yellow]Exit the program..[/yellow]")
        break