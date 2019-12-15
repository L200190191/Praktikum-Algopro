from Tkinter import Tk, Label, Button
from tkMessageBox import showinfo

my_app = Tk(className="Aplikasi Data Diri")
kiri1 = Label(my_app, text="Data diri", font=("Arial", 24))
kiri1.grid(row=0,column=0,sticky="W")

kiri2 = Label(my_app, text="Nama")
kiri2.grid(row=1,column=0,sticky="W")

kanan2 = Label(my_app, text="Kurnia Indah Nur Cahyani")
kanan2.grid(row=1,column=1,sticky="W")

kiri3 = Label(my_app, text="NIM")
kiri3.grid(row=2,column=0,sticky="W")

kanan3 = Label(my_app, text="L200190191")
kanan3.grid(row=2,column=1,sticky="W")

kiri4 = Label(my_app, text="Buku Favorit")
kiri4.grid(row=3,column=0,sticky="W")

kanan4 = Label(my_app, text="Komik")
kanan4.grid(row=3,column=1,sticky="W")

kiri5 = Label(my_app, text="Idola di kalangan sahabat")
kiri5.grid(row=4,column=0,sticky="W")

kanan5 = Label(my_app, text="Umar bin Khattab")
kanan5.grid(row=4,column=1,sticky="W")

kiri6 = Label(my_app, text="Motto")
kiri6.grid(row=5,column=0,sticky="W")

kanan6 = Label(my_app, text="Hidup Bahagia")
kanan6.grid(row=5,column=1,sticky="W")

def tutup():
    my_app.destroy()

B = Button(my_app, text="tutup", command=tutup)
B.grid(row=6, column=0)
my_app.mainloop()
