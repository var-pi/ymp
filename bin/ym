#! /run/current-system/sw/bin/zsh

song_title=$(ls $HOME/.ymp-store/library | fzf)
song_path="$HOME/.ymp-store/library/$song_title"
ffplay -nodisp $song_path
