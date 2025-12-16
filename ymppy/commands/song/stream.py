import subprocess

from ymppy.utils import prompt
from ymppy.utils import mkdirp, yt_dlp, url

def stream():
    # 1. Start yt-dlp as a source of raw bytes (no text=True, no log looping)
    # Use -f bestaudio to avoid the need for post-processing (-x)
    ytdlp_proc = subprocess.Popen(
        ["yt-dlp", "-f", "bestaudio", "-o", "-", url()],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL, # Keep the terminal clean
    )

    # 2. Start ffplay as the sink
    # Connect its stdin directly to yt-dlp's stdout
    ffplay_proc = subprocess.Popen(
        ["ffplay", "-nodisp", "-autoexit", "-i", "-"],
        stdin=ytdlp_proc.stdout
    )

    try:
        # Wait for the player to finish or the user to close it
        ffplay_proc.wait()
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        ytdlp_proc.terminate()
        ffplay_proc.terminate()
