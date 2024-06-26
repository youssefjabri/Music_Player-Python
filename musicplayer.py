from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()

class MusicPlayer():
    root.configure(bg='#fcfcec')
    root.geometry("450x150")
    def __init__(self, window) :
        def des():
            mixer.music.stop()
            Load.destroy()
            Play.destroy()
            Pause.destroy()
            Stop.destroy()
            Close.destroy()

        window.title('Music Player - Python'); 
        window.resizable(False,False)

        Load =  Button(window, text = 'Load',  width = 10, command = self.load,  bg='#4b7fa4', fg="#fcfcec", font=("calibri", 20), borderwidth=0, relief='flat')
        Play =  Button(window, text = 'Play',  width = 10, command = self.play,  bg='#088948', fg="#fcfcec", font=("calibri", 20), borderwidth=0, relief='flat')
        Pause = Button(window, text = 'Pause', width = 10, command = self.pause, bg='#FCBE25', fg="#fcfcec", font=("calibri", 20), borderwidth=0, relief='flat')
        Stop =  Button(window, text = 'Stop',  width = 10, command = self.stop,  bg='#cb464e', fg="#fcfcec", font=("calibri", 20), borderwidth=0, relief='flat')
        Close = Button(window, text = 'Close', width = 10, command = des,        bg='#cb464e', fg="#fcfcec", font=("calibri", 20), borderwidth=0, relief='flat')
        Load.place(x=0,y=20);Play.place(x=150,y=20);Pause.place(x=300,y=20);Close.place(x=150,y=75)

        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
        print(self.music_file)

    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file) 
            mixer.music.play()

    def pause(self):
        if not self.playing_state :
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False

    def stop(self):
        mixer.music.stop()

app = MusicPlayer(root)
root.mainloop()