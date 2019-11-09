Python 2.7.8 (default, Jun 30 2014, 16:08:48) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Kurnia Indah Nur Cahyani'
>>> NIM = 191
>>> Tinggi = 1.60
>>> Berat = 65
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<type 'tuple'>
>>> #Karena ditulis dalam kurung biasa , dipisahkan dengan tanda koma dan elemen tuple tidak dapat diubah
>>> Aku[0]
2000
>>> #Karena objek pertama dalam data "Aku" adalah "TahunLahir" dan nilai TahunLahir adalah 2000
>>> a = NIM % 4; Aku[a]
191
>>> #Karena sisa hasil pembagian dari 191 dibagi 4 adalah 3 jadi hasil dari aku (a) adalah 191
>>> type(Aku[a])
<type 'int'>
>>> #Karena nilai "TahunLahir" adalah 0, 0 adlah tipe data integer
>>> Aku[a:4]
(191,)
>>> #Karena 4 objek pertama adalah (191,)
>>> type(Aku[4])
<type 'str'>
>>> #Karena data pada Aku[4] berupa huruf dan ditulis demgan tanda kutip tunggal
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #Karena data Aku bertipe tuple, dan data tuple tidak dapat diubah
>>> type(Data)
<type 'list'>
>>> #Karena menggunakan kurung siku dan datanya dapat diubah
>>> type(Data[4])
<type 'str'>
>>> #Karena data pada Data[4] berupa huruf dan ditulis demgan tanda kutip tunggal
>>> Data[4][5]
'a'
>>> #Karena menampilkan Data ke-4 yaitu Nama pada urutan ke 5 yaitu huruf 'a'
>>> Data[4][a:6]
'nia'
>>> #Karena menampilkan Data ke-4 yaitu Nama yang diambil tiga huruf dari urutan ke 6
>>> Data[0] = 'ok'; Data
['ok', 65, 1.6, 191, 'Kurnia Indah Nur Cahyani']
>>> #karena menyisipkan string 'ok' pada urutan ke 0 di dalam Data
>>> Data[-a]
1.6
>>> #karena menampilkan Data urutan ke tiga dari belakang yaitu Tinggi
>>> range(a)
[0, 1, 2]
>>> #karena 'a' memiliki jangkauan 3
>>> 
