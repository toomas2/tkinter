#toomas
#17.01.2023
#tkinter kt 3.2

from tkinter import *
from tkinter import ttk

#aken
aken = Tk()
aken.title('jänkud')
aken.geometry("200x200")



def ringid1():
    height = float(sisestus.get())
    return ringid1

def arv_por():
    ringid = float(sisestus.get())
    ring = 0
    porgand = 0
    while ring < ringid:
        ring +=1
        if ring %2 == 0:
            porgand+=ring
            silt = Label(aken, text=porgand, font=("Arial", 10), padx=30)
            silt.grid(row=1,column=1,  sticky=W)
            
            
silt = Label(aken, text="Ringide arv:")
silt.grid(row=0,column=0, sticky=W)

silt2 = Label(aken, text="Vastus: ")
silt2.grid(row=1,column=0, sticky=W)

sisestus = Entry(aken, width=10, justify='center')
sisestus.grid(row=0,column=1)

nupp = Button(text="Arvuta!", padx=10, pady=5, command=arv_por)
nupp.grid(row=2, column=1)








aken.mainloop()