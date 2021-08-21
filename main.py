from time import sleep
from tkinter import Tk,Button,Label,Frame,RIGHT,LEFT, mainloop
from pygame import mixer
from keyboard import on_press, on_release,wait
from threading import Thread

flag ="sound1.mp3"
mixer.init()

def tune():
    global flag
    mixer.music.load(flag)
    mixer.music.play()
    def note(a):
        mixer.music.play()
    on_release(callback = note)
    wait()
    
def start():
    stbt.pack_forget()
    widget_list = w.winfo_children()
    for item in widget_list :
        if item.winfo_children() :
            widget_list.extend(item.winfo_children())
    for item in widget_list:
        item.pack_forget()
        
    x= Thread(target=tune)
    x.setDaemon(True)
    x.start()
    
    stop = Button(w,text="STOP",bg="red",font=" impact 20 bold",bd=8,command= lambda : w.destroy())
    info = Label(w,text="Costum tune and integreted music player is\ncomming Soon...")
    info.pack()
    stop.pack()
    

def sound1():
    global flag
    mixer.music.load("sound1.mp3")
    mixer.music.play()
    flag="sound1.mp3"
    stbt.pack()

def sound2():
    global flag
    
    mixer.music.load("sound2.mp3")
    mixer.music.play()
    flag="sound2.mp3"
    stbt.pack()

def sound3():
    global flag
    
    mixer.music.load("sound3.mp3")
    mixer.music.play()
    flag="sound3.mp3"
    stbt.pack()

def sound4():
    global flag
    
    mixer.music.load("sound4.mp3")
    mixer.music.play()
    flag = "sound4.mp3"
    stbt.pack()

w = Tk()
w.title("Mechvibe v-0.1.2")

f1 = Frame(w)
f2 = Frame(w)
l1 = Label(w,text="Select the tune",font="impact 36 bold")
b1 = Button(f1,text="tune 1",command = sound1,bd=8,)
b2 = Button(f1,text="tune 2",command= sound2,bd=8)
b3 = Button(f2,text="tune 3",command= sound3,bd=8)
b4 = Button(f2,text="tune 4",command= sound4,bd=8)

l1.pack()
f1.pack()
f2.pack()
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=LEFT)
b4.pack(side=RIGHT)

stbt =Button(w,text="START.",font=" impact 20 bold",bg="pale green",command= start,bd=8)

w.iconbitmap("icon.ico")
w.mainloop()