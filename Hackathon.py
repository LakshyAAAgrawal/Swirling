from tkinter import *
from tkinter import ttk
import os
import glob
#https://www.youtube.com/watch?v=R4AbzwYOmNE
#https://www.youtube.com/watch?v=pbIiIC6zN68
#https://www.youtube.com/watch?v=XSs2cR2Tvuk Avicii instrumental
#https://m.youtube.com/watch?v=9Aebjmgn0bw # believer
#https://m.youtube.com/watch?v=MvIwx0JThsk tay
import t1
import threading

def cl():
    thr=threading.Thread(target=click)
    t1.play=True
    thr.start()
def click():
    print("Hey")
    os.system("youtube-dl -x --audio-format wav " + textentry.get())
    for filename in glob.glob('*.wav'):
        print(filename)
        t1.play_song(filename)

def stop():
    t1.play=False
def stop2():
    thr._stop()
    for filename in glob.glob('*.wav'):
        print(filename)
window=Tk()
photo1=PhotoImage(file="music.png")

thr=threading.Thread(target=click)
window.title("Music Player")
window.configure(background="black")
Button(window, text="Play", width=4, command=cl).grid(row=6, column=0, sticky=W)
Button(window, text="Stop", width=4, command=stop).grid(row=6, column=0, sticky=E)
#Button.pack(side=BOTTOM)
Label(window, text="Enter your YouTube link:", bg="black", fg="white", font="none 11 bold") .grid(row=2, column=0, sticky=N)

textentry=Entry(window, width=20, bg="blue")
textentry.grid(row=4, column=0, sticky=S)




Label (window, image=photo1, bg="black").grid(row=0, column=0, sticky=N)
window.mainloop()
