from tkinter import  Tk,Button,Label,Frame,filedialog,ttk,DoubleVar,PhotoImage,RIGHT,LEFT
from pygame import mixer
from threading import Thread

mixer.init()
tune = mixer.Sound("sound1.mp3")
vol = 1.0
w = Tk()
w.title("Mechvibe v-1.1.2")
track = 0
vibe_vol_value = DoubleVar()
music_vol_value = DoubleVar()
music_vol_value.set(1.0)
vibe_vol_value.set(1.0)
iplay = PhotoImage(file="play.png")
ipause = PhotoImage(file="pause.png")
#mixer.Channel(1).play(mixer.Sound("C:\\Users\\tomin\\Desktop\\chirakukal.mp3"))

def vibe_vol_change(e):
    mixer.Channel(0).set_volume(vibe_vol_value.get())

def music_vol_change(e):
    mixer.Channel(1).set_volume(music_vol_value.get()*0.3)

def tune_():
    global tune
    def note(a):
        mixer.Channel(0).play(tune)
    from keyboard import on_release,wait
    on_release(callback = note)
    wait()
    
def strt():
    x= Thread(target=tune_)
    x.setDaemon(True)
    x.start()
    start.grid_forget()
    stop.grid(row=1,column=1)

def track_select():
    global track
    play_.pack_forget()
    pause_.pack()
    track = mixer.Sound(filedialog.askopenfile(title="select the tune",filetypes=(("mp3 files(1 sec recommended)","*.mp3"),)))
    mixer.Channel(1).play(track)   

def music_play():
    global track
    if track:
        play_.pack_forget()
        pause_.pack()
        mixer.Channel(1).unpause()

def music_pause():
    pause_.pack_forget()
    play_.pack()
    mixer.Channel(1).pause()   

def sound1():
    global tune
    tune= mixer.Sound("sound1.mp3")
    mixer.Channel(0).play(tune)
    
def sound2():
    global tune
    tune= mixer.Sound("sound2.mp3")
    mixer.Channel(0).play(tune)

def sound3():
    global tune
    tune= mixer.Sound("sound3.mp3")
    mixer.Channel(0).play(tune)

def sound4():
    global tune
    tune= mixer.Sound("sound4.mp3")
    mixer.Channel(0).play(tune)

def custom():
    global tune
    tune = mixer.Sound(filedialog.askopenfile(title="select the tune",filetypes=(("mp3 files(1 sec recommended)","*.mp3"),)))


#Frames
f4 = Frame(w)
f0 = Frame(f4)    
f1 = Frame(f0)
f2 = Frame(f0)
f3 = Frame(f4)
f5 = Frame(w)
f6 = Frame(f5)
f7 = Frame(f5)
#Labels
l1 = Label(w,text="Select the tune",font="impact 36 bold")
l2 = Label(f0,text="Vibe")
l3 = Label(f3,text="Vol",width=5)
l4 = Label(f7,text="Music")
l5 = Label(f6,text="Vol",width=5)
#Buttons
b1 = Button(f1,text="tune 1",command = sound1,bd=4,)
b2 = Button(f1,text="tune 2",command= sound2,bd=4)
b3 = Button(f2,text="tune 3",command= sound3,bd=4)
b4 = Button(f2,text="tune 4",command= sound4,bd=4)
b5 = Button(f0,text="add tune",command= custom,bd=4)
b6 = Button(f7,text="browse",command=track_select,bd=4)
play_ =Button(f7,image=iplay,borderwidth=0,command=music_play)
pause_=Button(f7,image=ipause,borderwidth=0,command=music_pause)
start =Button(w,text="START.",font=" impact 20 bold",bg="pale green",command= strt,bd=4)
stop = Button(w,text="STOP",bg="red",font=" impact 20 bold",bd=4,command= lambda : w.destroy())
#Slider
vibeVol = ttk.Scale(f3,from_=1,to=0,orient='vertical',command=vibe_vol_change,variable=vibe_vol_value)
musicVol = ttk.Scale(f6,from_=1,to=0,orient='vertical',command=music_vol_change,variable=music_vol_value)
#layout
l1.grid(row=0,column=1)
l2.pack()
l3.pack(pady=3)
l4.pack()
l5.pack(pady=3)
f0.grid(row=0,column=1)
f1.pack()
f2.pack()
f3.grid(row=0,column=0)
f4.grid(row=1,column=0)
f5.grid(row=1,column=2)
f6.pack(side=RIGHT)
f7.pack(side=LEFT)
musicVol.pack()
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=LEFT)
b4.pack(side=RIGHT)
b5.pack()
b6.pack()
play_.pack()
start.grid(row=1,column=1)
vibeVol.pack()

w.iconbitmap("icon.ico")
w.minsize(400,250)
w.resizable(False,False)
w.mainloop()