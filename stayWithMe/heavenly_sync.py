import time
from rich.console import Console
from rich.panel import Panel

console = Console()

# ===============================
# CONFIG
# ===============================
CHAR_SPEED = 0.047
POLL_SPEED = 0.001
PAUSE_AFTER_LINE = 0.06

# ===============================
# RAW LYRICS (delays between lines)
# ===============================
raw_lyrics = [
    (1.0, "Stay with me (stay with me)"),
    (1.55, "Please don't leave (please don't leave)"),
    (1.65, "Say you need me, need me, need"),
    (1.85, "Cause I can't breathe, can't breathe"),
    (1.95, "Stay with me (stay with me)"),
    (2.05, "Don't let go (don't let go)"),
    (2.10, "If you leave me, leave me, leave"),
    (2.20, "I'll be alone, alone"),
]

# تحويل delays إلى timestamps تراكمية
lyrics = []
current_time = 0.0

for delay, line in raw_lyrics:
    current_time += delay
    lyrics.append((float(f"{current_time:.2f}"), line))

# ===============================
# UI HELPERS
# ===============================
def boot_screen():
    console.clear()
    console.print()
    console.print(
        Panel(
            "[bold cyan]HEAVENLY SYNC ENGINE[/bold cyan]\n"
            "[dim]Initializing lyric timing protocol...[/dim]",
            border_style="bright_blue",
            padding=(1, 4),
            expand=False
        )
    )
    time.sleep(0.9)

    console.print("[cyan]› loading audio mood[/cyan]")
    time.sleep(0.45)
    console.print("[magenta]› mapping heartbeat to terminal[/magenta]")
    time.sleep(0.45)
    console.print("[yellow]› syncing emotional damage...[/yellow]")
    time.sleep(0.65)

    console.print()
    console.print("[bold green]STATUS:[/bold green] READY")
    time.sleep(0.8)
    console.clear()

def build_progress_bar(progress, total_blocks=26):
    filled = int(progress * total_blocks)
    empty = total_blocks - filled
    return f"[{'█' * filled}{'░' * empty}]"

def pre_intro_animation(duration=14.0):
    frames = ["◜", "◝", "◞", "◟"]
    messages = [
        "[cyan]› loading audio mood[/cyan]",
        "[magenta]› mapping heartbeat to terminal[/magenta]",
        "[yellow]› syncing emotional damage...[/yellow]",
        "[green]› scanning vocal horizon[/green]",
        "[bright_cyan]› buffering heartbreak packets[/bright_cyan]",
        "[white]› locking lyric stream[/white]",
        "[blue]› routing signal through memory lanes[/blue]",
        "[red]› stabilizing emotional frequency[/red]",
    ]

    fake_logs = [
        "[dim]log:[/dim] waveform detected",
        "[dim]log:[/dim] beat pattern stable",
        "[dim]log:[/dim] vocal channel isolated",
        "[dim]log:[/dim] sync confidence rising",
        "[dim]log:[/dim] terminal resonance detected",
        "[dim]log:[/dim] lyric engine armed",
    ]

    start = time.perf_counter()
    i = 0

    while (time.perf_counter() - start) < duration:
        elapsed = time.perf_counter() - start
        remaining = max(0.0, duration - elapsed)
        progress = min(elapsed / duration, 1.0)

        frame = frames[i % len(frames)]
        msg = messages[i % len(messages)]
        log1 = fake_logs[i % len(fake_logs)]
        log2 = fake_logs[(i + 2) % len(fake_logs)]
        bar = build_progress_bar(progress)

        console.clear()
        console.print()
        console.print(
            Panel(
                "[bold cyan]HEAVENLY SYNC ENGINE[/bold cyan]\n"
                "[dim]Initializing lyric timing protocol...[/dim]",
                border_style="bright_blue",
                padding=(1, 4),
                expand=False
            )
        )

        console.print(msg)
        console.print(log1)
        console.print(log2)
        console.print()
        console.print(f"[bold green]STATUS:[/bold green] READY  [dim]{frame}[/dim]")
        console.print(f"[bold cyan]SYNC[/bold cyan]  {bar}  [white]{int(progress * 100):02d}%[/white]")
        console.print("[bold bright_black]────────────────────────────────────────────[/bold bright_black]")
        console.print("[bold cyan]Track[/bold cyan]: [white]HEAVENLY JUMPSTYLE[/white]")
        console.print("[bold cyan]Mode[/bold cyan] : [white]Lyric Sync / Terminal Performance[/white]")
        console.print("[bold cyan]State[/bold cyan]: [green]LIVE[/green]")
        console.print("[bold bright_black]────────────────────────────────────────────[/bold bright_black]")
        console.print(f"[dim]vocals begin in {remaining:0.1f}s[/dim]")

        time.sleep(0.18)
        i += 1

    console.clear()

def header():
    console.print("[bold bright_black]────────────────────────────────────────────[/bold bright_black]")
    console.print("[bold cyan]Track[/bold cyan]: [white]HEAVENLY JUMPSTYLE[/white]")
    console.print("[bold cyan]Mode[/bold cyan] : [white]Lyric Sync / Terminal Performance[/white]")
    console.print("[bold cyan]State[/bold cyan]: [green]LIVE[/green]")
    console.print("[bold bright_black]────────────────────────────────────────────[/bold bright_black]")
    console.print()

def type_line(text: str, style: str = "bold yellow"):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(CHAR_SPEED)
    console.print()
    time.sleep(PAUSE_AFTER_LINE)

def cinematic_outro():
    console.print()
    console.print("[bold bright_black]────────────────────────────────────────────[/bold bright_black]")
    time.sleep(0.20)
    console.print("[bold cyan]stream closed[/bold cyan] ...")
    time.sleep(0.30)
    console.print("[bold magenta]emotion buffer saved[/bold magenta] ...")
    time.sleep(0.30)
    console.print("[bold yellow]terminal left alone[/bold yellow] ...")
    time.sleep(0.55)
    console.print("[bold bright_black]────────────────────────────────────────────[/bold bright_black]")

# ===============================
# MAIN
# ===============================
def main():
    boot_screen()
    pre_intro_animation(duration=14.0)
    header()

    start_time = time.perf_counter()

    for i, (timestamp, line) in enumerate(lyrics, start=1):
        while (time.perf_counter() - start_time) < timestamp:
            time.sleep(POLL_SPEED)

        if i in (1, 5):
            style = "bold bright_cyan"
        elif i in (2, 6):
            style = "bold yellow"
        elif i in (3, 7):
            style = "bold magenta"
        else:
            style = "bold white"

        console.print(f"[dim]L{i:02}[/dim] ", end="")
        type_line(line, style=style)

    cinematic_outro()

if __name__ == "__main__":
    main()