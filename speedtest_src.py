# netspeed.py
import tkinter as tk
import speedtest
import threading
from pygame import mixer
u=0
d=0
def upload():
        global u
        s=speedtest.Speedtest()
        x=s.upload()
        u=" Upload Speed   : "+str(round(x/1024/1024,2))+" MBPS "
def download():
        global d
        s=speedtest.Speedtest()
        x=s.download()
        d=" Download Speed : "+str(round(x/1024/1024,2))+" MBPS "
def speed():
        file="assets\\music.mp3"
        mixer.init()
        mixer.music.load(file)
        mixer.music.play(loops=-1)
        top=tk.Toplevel()
        top.grab_set()
        top.config(bg="#040837")
        top.minsize(400,200)
        top.resizable(0,0)
        top.title("Speed Test (Made by Karan)")
        top.iconbitmap("assets\\icon.ico")
        f=tk.Label(top,bg="#040837")
        f.grid(row=0)


        dl=tk.Label(top,text=" Download Speed : ---- MBPS ",width=28)
        dl.grid(row=2,column=0,pady=22)
        dl.config(font=("Courier",17,"bold"),bg="#124576",fg="white")


        ul=tk.Label(top,text=" Upload Speed   : ---- MBPS ",width=28)
        ul.grid(row=3,column=0,pady=20)
        ul.config(font=("Courier",17,"bold"),bg="#124576",fg="white")
        
        b1.config(text="Calculating...")
        b1.update()
        t2=threading.Thread(target=upload,args=())
        t1=threading.Thread(target=download,args=())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        if d or u:
                dl.config(text=d)
                ul.config(text=u)
        else:
                dl.config(text="Cannot Connect")
                ul.config(text="Cannot Connect")
        dl.update()
        ul.update()
        b1.config(text="Calculate Speed")
        b1.update()
        mixer.music.pause()




root=tk.Tk()
label=tk.Label(text="Speed Calculator")
label.config(font=("Courier",30,"bold"),width=17,bg="white",fg="#040837")
label.grid(row=1,column=1,pady=50)


b1=tk.Button(text="Calculate Speed",command=speed)
b1.config(font=("Courier",25,"bold"),width=16,bg="#124576",fg="white",relief="raised",bd=10)
b1.grid(row=2,column=1,pady=20)



b2=tk.Button(text="Exit",command=root.quit)
b2.config(font=("Courier",25,"bold"),width=16,bg="#124576",fg="white",relief="raised",bd=10)
b2.grid(row=3,column=1,pady=20)


root.config(bg="#040837")
root.minsize(400,400)
root.resizable(0,0)
root.title("Speed Test (Made by Karan)")
root.iconbitmap("assets\\icon.ico")
root.mainloop()