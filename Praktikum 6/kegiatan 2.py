##Program Akun
##Dibuat oleh Kurnia Indah L200190191
import random
angka = random.randint(0,1000)

Nama = 'Kurnia Indah Nur Cahyani'
Tanggallahir = '20 November 2000'
NamaSingkat = Nama[0] + '.' + Nama[7] + '.' + Nama[13] + '_' + Nama[17:24]
Username = Nama[0] + Tanggallahir[0:2] + Tanggallahir[12:16]
Password = Nama[0:3] + str(angka)

print(Nama)
print(Tanggallahir)
print(NamaSingkat)
print(Username)
print(Password)
