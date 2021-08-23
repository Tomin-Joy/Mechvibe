from time import sleep
from tkinter import Pack, Tk,Button,Label,Frame,filedialog,RIGHT,LEFT,CENTER
from tkinter.constants import BOTTOM
from pygame import mixer
from keyboard import on_press, on_release,wait
from threading import Thread

flag ="sound1.mp3"
vol = 1.0
mixer.init()
w = Tk()
w.title("Mechvibe v-0.1.2")

def vol_up():
    global vol
    vol = (vol*10 + 1)/10
    if vol>1:
        vol=1
    print(vol)
    mixer.music.set_volume(vol)

def vol_down():
    global vol
    vol = (vol*10 - 1)/10
    if vol<0:
        vol=0
    print(vol)
    mixer.music.set_volume(vol)

def tune():
    global flag
    mixer.music.load(flag)
    mixer.music.play()
    def note(a):
        mixer.music.play()
    on_release(callback = note)
    wait()
    
def strt():
    x= Thread(target=tune)
    x.setDaemon(True)
    x.start()
    start.pack_forget()
    stop.pack(side=BOTTOM)
    

def sound1():
    global flag
    mixer.music.load("sound1.mp3")
    mixer.music.play()
    flag="sound1.mp3"

def sound2():
    global flag
    
    mixer.music.load("sound2.mp3")
    mixer.music.play()
    flag="sound2.mp3"

def sound3():
    global flag
    
    mixer.music.load("sound3.mp3")
    mixer.music.play()
    flag="sound3.mp3"

def sound4():
    global flag
    
    mixer.music.load("sound4.mp3")
    mixer.music.play()
    flag = "sound4.mp3"

def custom():
    global flag
    
    flag = filedialog.askopenfile(title="select the tune",filetypes=(("mp3 files(1 sec recommended)","*.mp3"),))

#Frames
f0 = Frame(w)    
f1 = Frame(f0)
f2 = Frame(f0)
f3 = Frame(w)
#Labels
l1 = Label(w,text="Select the tune",font="impact 36 bold")
l2 = Label(f0,text="Vibe")
l3 = Label(f3,text="Vol",width=5)
#Buttons
b1 = Button(f1,text="tune 1",command = sound1,bd=4,)
b2 = Button(f1,text="tune 2",command= sound2,bd=4)
b3 = Button(f2,text="tune 3",command= sound3,bd=4)
b4 = Button(f2,text="tune 4",command= sound4,bd=4)
b5 = Button(f0,text="add tune",command= custom,bd=4)
start =Button(f0,text="START.",font=" impact 20 bold",bg="pale green",command= strt,bd=4)
stop = Button(f0,text="STOP",bg="red",font=" impact 20 bold",bd=4,command= lambda : w.destroy())
volUp = Button(f3,text="+",height=4,width=3,command=vol_up,bd=4)
volDown = Button(f3,text="-",height=4,width=3,command=vol_down,bd=4)

l1.grid(row=0,column=1)
l2.pack()
l3.pack(pady=5)
f0.grid(row=1,column=1)
f1.pack()
f2.pack()
f3.grid(row=1,column=0)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=LEFT)
b4.pack(side=RIGHT)
b5.pack()
start.pack()
volUp.pack()
volDown.pack()




w.iconbitmap("icon.ico")
w.minsize(400,200)
w.mainloop()
