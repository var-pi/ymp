# ymp — YouTube Music Player

`ymp` (YouTube Music Player) is a small command-line tool for downloading and playing music from the terminal using `yt-dlp`, `fzf`, and `ffmpeg`, with a simple Typer-based interface.

## Features
- [x] Zsh autocompletions provided by `typer`.
- [x] Audio library and playlist folders managed automatically.
- [x] Download audio with `fzf` and `yt-dlp` (with `ytsearch`).
- [x] Delete audio with `fzf`.
- [x] Choose audio track with `fzf` and play with `ffmpeg`.
- [x] Choose audio track with `fzf` and stream with `ffmpeg`.
- [x] Create playlists with an interactive prompt.
- [x] Delete playlists with `fzf`.
- [x] Append tracks to a plylist with `fzf`.
- [x] Prune playlist from tracks with `fzf`.
- [x] Choose a playlist with `fzf` and play with `ffmpeg`.
- [x] Optional looping of song and playlist playback via `--loop` flag.
- [x] Only "non-playlisted" tracks are appendable to a playlist.
- [x] Use `ymp` shell instead of typing prefix `ymp` every time.
- [x] Delete a song from playlist before deleting from library.
- [ ] Pull songs in bulk from a plylist.
- [ ] Link several songs to a playlist.
- [ ] Unlink several songs from a playlist.
- [ ] Better interface.
- [ ] Quicker song downloading.
- [ ] Stop, play, skip, send to background.

## Library Location
Music is stored in:
```
~/.ymp-store/library
```

## Usage
```
ymp <command> [OPTIONS]
```

## Installation

>  The Nix setup wraps the script and provides all runtime dependencies.

### Option 1: Using Nix build (flake)

Build the package:
```
nix build
```
The binary will be in the `result` direectory: 
```
./result/bin/ymp
```

### Option 2: Using Nix flake

In the system flake add a link to the project:
```
ymp.url = "github:var-pi/ymp";
```
Now add the packages to system packages:
```
inputs.ymp.packages.${stdenv.hostPlatform.system}.default
```
Rebuild the flake. In the shell, `ymp` is in `PATH` and can be run directly:
```
ymp
```

## License
MIT
