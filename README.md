# ymp — YouTube Music Player

`ymp` (YouTube Music Player) is a small command-line tool for downloading and playing music from the terminal using `yt-dlp`, `fzf`, and `ffmpeg`, with a simple Typer-based interface.

## Features
- [x] Download audio from YouTube (single videos) into a local library
- [x] Interactive selection of tracks via `fzf`
- [x] Playback via `ffplay`
- [x] Play on a loop
- [ ] Create playlists
- [ ] Listen to playlists

## Library Location
Music is stored in:
```
~/.ymp-store/library
```

## Usage
```
ymp play
ymp download <URL>
```

## Installation

### Option 1: Run directly (no Nix required)
Ensure the following are available in `PATH`:
- Python 3
- `yt-dlp`
- `ffmpeg` (for `ffplay`)
- `fzf`

Then:
```
chmod +x ymp.py
./ymp.py play
./ymp.py download <URL>
```

### Option 2: Using Nix (flake)
Build and run:
```
nix build
./result/bin/ymp play
```

Or enter a development shell:
```
nix develop
ymp play
```

The Nix setup wraps the script and provides all runtime dependencies.

## Notes
- Only single videos are downloaded (`--no-playlist`).
- Audio is extracted and stored as Opus.
- Cancelling `fzf` exits cleanly without error.

## License
MIT
