# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 21:38:48 2017
"""
import math

import Tkinter

root = Tkinter.Tk()

w = 600 # width for the Tk root
h = 500 # height for the Tk root


frame = Tkinter.Frame(root, width=w, height=h)
frame.pack()


# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)


global array1,array2,array3


#array1 berisi rating
array1=(89,
        89,
        91,
        92,
        87
);
#array2 berisi umur(tahun)
array2=(4,
        3,
        6,
        6,
        6
);

#array3 berisi harga
array3=(185,
        180,
        190,
        200,
        180);
        
datatest1=90
datatest2=5
datatest3=0
knn=3
print "\n"
print "|Rating|Umur|harga|"
for i in range(0,5):
    print i+1,
    print array1[i],
    print array2[i],
    print array3[i]

def perhitungan():
    global arrayjawab
    arrayjawab=();
    
    datatest1=int(dataset1.get())
    datatest2=int(dataset2.get())
    datatest3=0
    dataset3.set("")
    
    print "\n\n"
    for i in range(0,5):
        temp=(((datatest1-array1[i])**2)+((datatest2-array2[i])**2))**1/2
        arrayjawab = list(arrayjawab)
        arrayjawab.append(temp)
        arrayjawab = tuple(arrayjawab)
        print i+1,":",
        print arrayjawab[i]
    arrayjawab=list(arrayjawab)
    c=[]
    for i in range(0,3):
        c.append(min(arrayjawab))        
        arrayjawab.remove(min(arrayjawab))
        print c[i]
    
    hargas=[]
    temp=(((datatest1-array1[0])**2)+((datatest2-array2[0])**2))**1/2
    g=len(c)
    print "sisa di c:",g
    if g!=0:  
        try:
            if temp==c[0]:
                hargas.append(array3[0])
                c.remove(temp)
            elif temp==c[1]:
                hargas.append(array3[0])
                c.remove(temp)
            elif temp==c[2]:
                hargas.append(array3[0])
                c.remove(temp)
        except IndexError:
            print "none"
    
    temp=(((datatest1-array1[1])**2)+((datatest2-array2[1])**2))**1/2
    g=len(c)
    print "sisa di c:",g
    if g!=0:
        try:        
            if temp==c[0]:
                hargas.append(array3[1])
                c.remove(temp)
            elif temp==c[1]:
                hargas.append(array3[1])
                c.remove(temp)
            elif temp==c[2]:
                hargas.append(array3[1])
                c.remove(temp)
        except IndexError:
            print "none"
        
        
    temp=(((datatest1-array1[2])**2)+((datatest2-array2[2])**2))**1/2
    g=len(c)
    print "sisa di c:",g
    if g!=0:  
        try:
            if temp==c[0]:
                hargas.append(array3[2])
                c.remove(temp)
            elif temp==c[1]:
                hargas.append(array3[2])
                c.remove(temp)
            elif temp==c[2]:
                hargas.append(array3[2])
                c.remove(temp)
        except IndexError:
            print "none"
    
    temp=(((datatest1-array1[3])**2)+((datatest2-array2[3])**2))**1/2
    g=len(c)
    print "sisa di c:",g
    if g!=0:  
        try:
            if temp==c[0]:
                hargas.append(array3[3])
                c.remove(temp)
            elif temp==c[1]:
                hargas.append(array3[3])
                c.remove(temp)
            elif temp==c[2]:
                hargas.append(array3[3])
                c.remove(temp)
        except IndexError:
            print "none"
            
    temp=(((datatest1-array1[4])**2)+((datatest2-array2[4])**2))**1/2
    g=len(c)
    print "sisa di c:",g
    if g!=0:    
        try:        
            if temp==c[0]:
                hargas.append(array3[4])
                c.remove(temp)
            elif temp==c[1]:
                hargas.append(array3[4])
                c.remove(temp)
            elif temp==c[2]:
                hargas.append(array3[4])
                c.remove(temp)
        except IndexError:
            print "none"
            
    print hargas
    print c
    total=0
    #hasilnya: harga dari data baru:
    for i in range(0,3):
        total+=hargas[i]
    total=total/knn
    print "harga dari data baru yaitu:",total
    dataset3.set(total)
#perhitungan()

labeled1=Tkinter.Label(frame,text="Menghitung Harga dengan K-Means:")
labeled1.config(font=("Courier",18))
labeled1.place(x=10, y=0, width=500, height=100)

labeled1=Tkinter.Label(frame,text="Rating:")
labeled1.place(x=10, y=100, width=100, height=20)
dataset1=Tkinter.StringVar() 
kotak1= Tkinter.Entry(frame,textvariable=dataset1)
kotak1.place(x=10, y=120, width=100, height=20) 
dataset1.set("")

labeled1=Tkinter.Label(frame,text="Umur:")
labeled1.place(x=120, y=100, width=100, height=20)
dataset2=Tkinter.StringVar() 
kotak2= Tkinter.Entry(frame,textvariable=dataset2)
kotak2.place(x=120, y=120, width=100, height=20) 
dataset2.set("")

labeled1=Tkinter.Label(frame,text="Harga:")
labeled1.place(x=240, y=100, width=100, height=20)
dataset3=Tkinter.StringVar() 
kotak3= Tkinter.Entry(frame,textvariable=dataset3)
kotak3.place(x=240, y=120, width=100, height=20) 
dataset3.set("")

button1=Tkinter.Button(frame,text="Start",command=perhitungan)
button1.place(x=180, y=180, width=120, height=20)


root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop()
