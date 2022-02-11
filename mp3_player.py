import pygame
import tkinter as tkr
import os

FONT = "Helvetica 12 bold"

music_player = tkr.Tk()
music_player.title("Homegrown MP3 Player")
music_player.geometry("600x600")

string_var = tkr.StringVar()
playlist = tkr.Listbox(music_player, font=FONT, highlightbackground="black", selectmode=tkr.SINGLE)


def build_song_list(mp3_playlist, directory="songs"):
    """
    Creates a list of songs and inserts them into the playlist for the mp3 player to play.
    :param directory: the directory containing the mp3 songs to play
    :param mp3_playlist: the playlist of songs
    """
    # changes current working dir to specified path
    os.chdir(directory)
    song_list = os.listdir()

    for item in song_list:
        position = 0
        # add the song to the playlist in the order it encountered it
        mp3_playlist.insert(position, item)
        position += 1


def play(mp3_playlist):
    """
    Plays the song that is next in the queue.
    :param mp3_playlist: the list of songs to play
    """
    # 'ACTIVE' is active state, aka file selected
    pygame.mixer.music.load(mp3_playlist.get(tkr.ACTIVE))
    string_var.set(mp3_playlist.get(tkr.ACTIVE))
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


def build_widgets(mp3_music_player, mp3_playlist):
    """
    Builds the buttons and display for the MP3 player and sets them up appropriately on the screen.
    :param mp3_playlist: the list of songs to play
    :param mp3_music_player: the tkinter music player object
    """
    play_button = tkr.Button(mp3_music_player, width=5, height=3, font=FONT, text="Play",
                             command=lambda: play(playlist),
                             highlightbackground="red",
                             fg="white")
    stop_button = tkr.Button(mp3_music_player, width=5, height=3, font=FONT, text="Stop", command=exit_music_player,
                             highlightbackground="purple", fg="white")
    pause_button = tkr.Button(mp3_music_player, width=5, height=3, font=FONT, text="Pause", command=pause,
                              highlightbackground="green", fg="white")
    unpause_button = tkr.Button(mp3_music_player, width=5, height=3, font=FONT, text="Unpause", command=unpause,
                                highlightbackground="blue", fg="white")

    song_title = tkr.Label(mp3_music_player, font=FONT, textvariable=string_var)

    # arrange the widgets
    song_title.pack()
    # makes all the widgets the same size as the container
    play_button.pack(fill="x")
    stop_button.pack(fill="x")
    pause_button.pack(fill="x")
    unpause_button.pack(fill="x")
    mp3_playlist.pack(fill="both", expand="yes")


build_song_list(playlist)
pygame.init()
pygame.mixer.init()

build_widgets(music_player, playlist)
music_player.mainloop()
