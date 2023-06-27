import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from playsound import playsound
import pygame
from pygame import mixer
import os
import time


IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
song_counter = 0
def setup():
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    musicWindow()
setup()
def musicWindow():
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")

    selectLabel = Label(window, text= "Select Song", bg="LightSkyBlue",font=("Calibri",8))
    selectLabel.place(x=2,y=1)

    listbox = Listbox(window,height=10,width=39,activestyle='dotbox',bg="LightSkyBlue",borderwidth=2,font=("Calibri",10))
    listbox.place(x=10,y=18)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command = listbox.yview)

    PlayButton=Button(window,text="Play", width=10,bd=1,bg='SkyBlue',font = ("Calibri",10), command=play)
    PlayButton.place(x=30,y=200)
    
    Stop=Button(window,text="Stop",bd=1,width=10,bg='SkyBlue', font = ("Calibri",10), command=stop)
    Stop.place(x=200,y=200)

    ResumeButton=Button(window,text="Resume",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10), command=resume)
    ResumeButton.place(x=30,y=250)

    PauseButton=Button(window,text="Pause",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10), command=pause)
    PauseButton.place(x=30,y=250)
    
    Upload=Button(window,text="Upload",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
    Upload.place(x=30,y=250)
    
    Download =Button(window,text="Download",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
    Download.place(x=200,y=250)
    
    infoLabel = Label(window, text= "",fg= "blue",bg='SkyBlue', font = ("Calibri",8))
    infoLabel.place(x=4, y=280)
    
    window.mainloop()

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter,filename)
        song_counter = song_counter+1

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected !=""):
        infoLabel.configure(text="Now Playing: "+song_selected)
    else:
        infoLabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
