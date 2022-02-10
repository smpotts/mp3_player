import pygame
import tkinter as tkr
import os

music_player = tkr.Tk()
music_player.title("Homegrown MP3 Player")
music_player.geometry("600x600")
font = "Helvetica 12 bold"

string_var = tkr.StringVar()
directory = "songs"
# changes current working dir to specified path
os.chdir(directory)
song_list = os.listdir()
playlist = tkr.Listbox(music_player, font=font, highlightbackground="black", selectmode=tkr.SINGLE)


def build_song_list():
    """
    Creates a list of songs and inserts them into the playlist for the mp3 player to plyy.
    """
    for item in song_list:
        position = 0
        # add the song to the playlist in the order it encountered it
        playlist.insert(position, item)
        position += 1


def play():
    """
    Plays the song that is next in the queue.
    """
    # 'ACTIVE' is active state, aka file selected
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    string_var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def exit_music_player():
    """
    Stops playing the song.
    :return:
    """
    pygame.mixer.music.stop()


def pause():
    """
    Pauses the song that is currently playing.
    :return:
    """
    pygame.mixer.music.pause()


def unpause():
    """
    Unpauses the song that has been paused.
    :return:
    """
    pygame.mixer.music.unpause()


def build_widgets():
    """
    Builds the buttons and display for the MP3 player and sets them up appropriately on the screen.
    """
    play_button = tkr.Button(music_player, width=5, height=3, font=font, text="Play", command=play,
                             highlightbackground="red",
                             fg="white")
    stop_button = tkr.Button(music_player, width=5, height=3, font=font, text="Stop", command=exit_music_player,
                             highlightbackground="purple", fg="white")
    pause_button = tkr.Button(music_player, width=5, height=3, font=font, text="Pause", command=pause,
                              highlightbackground="green", fg="white")
    unpause_button = tkr.Button(music_player, width=5, height=3, font=font, text="Unpause", command=unpause,
                                highlightbackground="blue", fg="white")

    song_title = tkr.Label(music_player, font=font, textvariable=string_var)

    # arrange the widgets
    song_title.pack()
    # makes all the widgets the same size as the container
    play_button.pack(fill="x")
    stop_button.pack(fill="x")
    pause_button.pack(fill="x")
    unpause_button.pack(fill="x")
    playlist.pack(fill="both", expand="yes")


build_song_list()
pygame.init()
pygame.mixer.init()

build_widgets()
music_player.mainloop()
