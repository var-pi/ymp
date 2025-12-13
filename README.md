# ymp — YouTube Music Player

`ymp` (YouTube Music Player) is a small command-line tool for downloading and playing music from the terminal using `yt-dlp`, `fzf`, and `ffmpeg`, with a simple Typer-based interface.

## Features
- [x] Download audio from YouTube (single videos) into a local library
- [x] Interactive selection of tracks via `fzf`
- [x] Playback via `ffplay`
- [x] Play on a loop
- [ ] Create playlists
- [x] Listen to playlists

## Library Location
Music is stored in:
```
~/.ymp-store/library
```

## Usage
```
ymp <command> [OPTIONS] [ARGS]
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
```

Now the binnary is accessible as follows:
```
./ymp.py
```

### Option 2: Using Nix (flake)

Build the package:
```
nix build
```

This produces an executable:
```
./result/bin/ymp
```

The binary will be in the `result` direectory: 
```
./result/bin/ymp
```

Alternatively, enter a development shell:
```
nix develop
```

In the shell, `ymp` is in `PATH` and can be run directly:
```
ymp
```

The Nix setup wraps the script and provides all runtime dependencies.

## Notes
- Only single videos are downloaded (`--no-playlist`).
- Audio is extracted and stored as Opus.
- Cancelling `fzf` exits cleanly without error.

## License
MIT
