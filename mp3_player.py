import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os


mp3_name = "Homegrown MP3 Player"
dimensions = "600x600"
font = "Helvetica 12 bold"
string_var = tkr.StringVar()
directory = askdirectory()
# changes current working dir to specified path
os.chdir(directory)
song_list = os.listdir()


class Mp3Player:
    def __init__(self):
        music_player = tkr.Tk()
        music_player.title(mp3_name)
        music_player.geometry(dimensions)
        self.playlist = tkr.Listbox(music_player,
                                    font=font,
                                    highlightbackground="black",
                                    selectmode=tkr.SINGLE)

        Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Play", command=self.play,
                             highlightbackground="red",
                             fg="white")
        Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Stop",
                             command=self.exit_music_player,
                             highlightbackground="purple", fg="white")
        Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Pause", command=self.pause,
                             highlightbackground="green", fg="white")
        Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="Unpause", command=self.unpause,
                             highlightbackground="blue", fg="white")

        song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=string_var)

        # arrange the widgets
        song_title.pack()
        # makes all the widgets the same size as the container
        Button1.pack(fill="x")
        Button2.pack(fill="x")
        Button3.pack(fill="x")
        Button4.pack(fill="x")
        self.playlist.pack(fill="both", expand="yes")

        music_player.mainloop()

    def build_song_list(self):
        for item in song_list:
            position = 0
            self.playlist.insert(position, item)
            position += 1

    def play(self):
        # active is active state, aka file selected
        pygame.mixer.music.load(self.playlist.get(tkr.ACTIVE))
        string_var.set(self.playlist.get(tkr.ACTIVE))
        pygame.mixer.music.play()

    @staticmethod
    def exit_music_player():
        pygame.mixer.music.stop()

    @staticmethod
    def pause():
        pygame.mixer.music.pause()

    @staticmethod
    def unpause():
        pygame.mixer.music.unpause()
