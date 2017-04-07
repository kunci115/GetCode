# -*- coding: utf-8 -*-

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


global array1,array2,array3,array4,array5
#jenis kelamin di array1
array1=("laki",
        "laki",
        "perempuan",
        "perempuan",
        "laki",
        "laki",
        "perempuan",
        "perempuan",
        "laki",
        "perempuan",
        "perempuan",
        "perempuan",
        "laki",
        "laki",
        "laki"
        );

#Status mahasiswa di array2
array2=("Mahasiswa",
        "Bekerja",
        "Mahasiswa",
        "Mahasiswa",
        "Bekerja",
        "Bekerja",
        "Bekerja",
        "Bekerja",
        "Bekerja",
        "Mahasiswa",
        "Mahasiswa",
        "Mahasiswa",
        "Bekerja",
        "Mahasiswa",
        "Mahasiswa",
        );    
        
#Status pernikahan di array3

array3=("Belum",
        "Belum",
        "Belum",
        "Menikah",
        "Menikah",
        "Menikah",
        "Menikah",
        "Belum",
        "Belum",
        "Menikah",
        "Belum",
        "Belum",
        "Menikah",
        "Menikah",
        "Belum",
        );
        
#IPK Semester di array4
array4=(3.17,
        3.30,
        3.01,
        3.25,
        3.20,
        2.50,
        3.00,
        2.70,
        2.40,
        2.50,
        2.50,
        3.50,
        3.30,
        3.25,
        2.30
        );
        
#Kategori di array5
array5=("Tepat",
        "Tepat",
        "Tepat",
        "Tepat",
        "Tepat",
        "Terlambat",
        "Terlambat",
        "Terlambat",
        "Terlambat",
        "Terlambat",
        "Terlambat",
        "Tepat",
        "Tepat",
        "Tepat",
        "Terlambat"
        );

for i in range(0,15):
    print i+1,
    print array1[i],
    print array2[i],
    print array3[i],
    print array4[i],
    print array5[i]
    #i nya maksnya sampai 14
   
global datatest1,datatest2,datatest3,datatest4,datatest5
#datatest1="laki"
#datatest2="Mahasiswa"
#datatest3="Belum"
#datatest4=2.70
#datatest5=""    
def perhitungan():
    global tepat,terlambat,tepat2,terlambat2
    global pembed1,pembed2,pembed3,pembed4,pembed5,pembed6,pembed7,pembed8
    datatest1=kotak1.get()
    datatest2=kotak2.get()
    datatest3=kotak3.get()
    datatest4=float(kotak4.get())
    datatest5=""
    tepat=0
    terlambat=0
    pembed1=0
    pembed2=0
    pembed3=0
    pembed4=0
    pembed5=0
    pembed6=0
    pembed7=0
    pembed8=0
    for i in range(0,15):
        if array5[i]=="Tepat":
            tepat+=1
        else:
            terlambat+=1
    
    print "P:Tepat=",
    print tepat,"/15"
    tepat2=tepat
    tepat=float(tepat)/float(15)
    print "P:Terlambat=",
    print terlambat,"/15"
    terlambat2=terlambat
    terlambat=float(terlambat)/float(15)
    
    for i in range(0,15):
        if array1[i]==datatest1 and array5[i]=="Tepat":
            pembed1+=1
        elif array1[i]==datatest1 and array5[i]=="Terlambat":
            pembed2+=1
    
    print "P1=tepat=",
    print pembed1,"/",tepat2
    
    print "P1=terlambat=",
    print pembed2,"/",terlambat2
    
    for i in range (0,15):
        if array2[i]==datatest2 and array5[i]=="Tepat":
            pembed3+=1
        elif array2[i]==datatest2 and array5[i]=="Terlambat":
            pembed4+=1
    
    print "P2=tepat=",
    print pembed3,"/",tepat2
    
    print "P2=terlambat=",
    print pembed4,"/",terlambat2
    
    for i in range (0,15):
        if array3[i]==datatest3 and array5[i]=="Tepat":
            pembed5+=1
        elif array3[i]==datatest3 and array5[i]=="Terlambat":
            pembed6+=1
    
    print "P3=tepat=",
    print pembed5,"/",tepat2
    
    print "P3=terlambat=",
    print pembed6,"/",terlambat2
    
    
    for i in range (0,15):
        if array4[i]==datatest4 and array5[i]=="Tepat":
            pembed7+=1
        elif array4[i]==datatest4 and array5[i]=="Terlambat":
            pembed8+=1
    
    print "P4=tepat=",
    print pembed7,"/",tepat2
    
    print "P4=terlambat=",
    print pembed8,"/",terlambat2
    
    print"\n\n"
    print "untuk var yang tepat"
    hasil1=((float(pembed1)/float(tepat2))*(float(pembed3)/float(tepat2))*(float(pembed5)/float(tepat2))*(float(pembed7)/float(tepat2)))*(float(tepat))
    print hasil1
    
    print"\n\n"
    print "untuk var yang terlambat"
    hasil2=((float(pembed2)/float(terlambat2))*(float(pembed4)/float(terlambat2))*(float(pembed6)/float(terlambat2))*(float(pembed8)/float(terlambat2)))*(float(terlambat))
    print hasil2
    print"\n\n"
    if(hasil1>hasil2):
        print "maka data baru masuk ke keterangan Tepat"
        datatest5="Tepat"
        dataset5.set(datatest5)
    elif hasil2>hasil1:
        print "maka data baru masuk ke keterangan Terlambat"
        datatest5="Terlambat"
        dataset5.set(datatest5)
    else:
        datatest5="tidak sesuai training data"
        dataset5.set(datatest5)
#perhitungan()
        
labeled1=Tkinter.Label(frame,text="Masukan Test data:")
labeled1.config(font=("Courier",30))
labeled1.place(x=10, y=0, width=500, height=100)

labeled1=Tkinter.Label(frame,text="Jenis Kelamin:")
labeled1.place(x=10, y=100, width=100, height=20)
dataset1=Tkinter.StringVar() 
kotak1= Tkinter.Entry(frame,textvariable=dataset1)
kotak1.place(x=10, y=120, width=100, height=20) 
dataset1.set("")

labeled1=Tkinter.Label(frame,text="Status Mahasiswa:")
labeled1.place(x=120, y=100, width=100, height=20)
dataset2=Tkinter.StringVar() 
kotak2= Tkinter.Entry(frame,textvariable=dataset2)
kotak2.place(x=120, y=120, width=100, height=20) 
dataset2.set("")        
        
labeled1=Tkinter.Label(frame,text="Status Pernikahan:")
labeled1.place(x=240, y=100, width=100, height=20)
dataset3=Tkinter.StringVar() 
kotak3= Tkinter.Entry(frame,textvariable=dataset3)
kotak3.place(x=240, y=120, width=100, height=20) 
dataset3.set("")        

labeled1=Tkinter.Label(frame,text="IPK 1-6 Semester:")
labeled1.place(x=360, y=100, width=100, height=20)
dataset4=Tkinter.StringVar() 
kotak4= Tkinter.Entry(frame,textvariable=dataset4)
kotak4.place(x=360, y=120, width=100, height=20) 
dataset4.set("")   


button1=Tkinter.Button(frame,text="Start",command=perhitungan)
button1.place(x=180, y=180, width=120, height=20)

labeled1=Tkinter.Label(frame,text="Masuk ke Kategori")
labeled1.place(x=180, y=220, width=120, height=20)
dataset5=Tkinter.StringVar() 
kotak5= Tkinter.Entry(frame,textvariable=dataset5)
kotak5.place(x=140, y=240, width=200, height=20) 
dataset5.set("")   

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop()
    
