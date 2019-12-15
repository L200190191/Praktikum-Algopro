from Tkinter import *

apl = Tk()
apl.title("Menghitung Luas Bangun Geometri")

def hitung():
    import math
    a = int(alas.get())
    t = int(tinggi.get())
    hasil = 0.5*a*t
    L5.config(text="Hasil = %s"%hasil)

L1 = Label(apl, text="Segitiga", font=('Arial', 24))
L1.grid(row=0, column=0, sticky="W")

L2 = Label(apl, text="Segitiga adalah bangun yang dapat dihitung luasnya")
L2.grid(row=1, column=0, columnspan=3, sticky="W")

L2a = Label(apl, text="Hanya membutuhkan alas dan tinggi")
L2a.grid(row=2, column=0, sticky="W")

L3 = Label(apl, text="Alas : ")
L3.grid(row=3, column=0, sticky="W")
alas= StringVar()
E3 = Entry(apl, textvariable=alas)
E3.grid(row=3, column=1, columnspan=2, sticky="W")

L4 = Label(apl, text="Tinggi :")
L4.grid(row=4, column=0, sticky="W")
tinggi = StringVar()
E4 = Entry(apl, textvariable=tinggi)
E4.grid(row=4, column=1, columnspan=2, sticky="W")

L5 = Label(apl, text="Hasil = 0", font=('Arial', 14, "bold"))
L5.grid(row=6, column=0, sticky="W")

B1 = Button(apl, text="Hitung Luas", command=hitung)
B1.grid(row=5, column=1, columnspan=2, sticky="W")
apl.mainloop()
