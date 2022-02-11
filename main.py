import mp3_player as mp3
import tkinter as tkr
import pygame


def main():
    music_player = tkr.Tk()
    music_player.title("Homegrown MP3 Player")
    music_player.geometry("500x500")

    string_var = tkr.StringVar()
    playlist = tkr.Listbox(music_player, font=mp3.FONT, highlightbackground="black", selectmode=tkr.SINGLE)
    mp3.build_song_list(playlist)
    pygame.init()
    pygame.mixer.init()

    mp3.build_widgets(music_player, playlist, string_var)
    music_player.mainloop()


if __name__ == "__main__":
    main()
