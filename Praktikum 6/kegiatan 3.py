Python 2.7.8 (default, Jun 30 2014, 16:08:48) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Kurnia Indah Nur cahyani'
>>> NIM = 'L200190191'
>>> X = '1' + NIM[7:]
>>> a =int(X)
>>> b = len(Nama)
>>> type(a)
<type 'int'>
>>> #Karena data "a" menyimpan data berupa bilangan bulat dan tidak mempenyai titik desimal (dan angka dibelakang koma koma desimal) dan bukan merupakan angka pecahan
>>> type(b)
<type 'int'>
>>> #Karena data "b" menyimpan data berupa len yang artinya menyimpan banyaknya huruf dalam variabel "Nama"
>>> a / b
49
>>> #Karena "a" adalah 1191 dan "b" banyaknya 24, 1191 dibagi 24 hasilnya 49.625 , dan data bertipe int maka hasilnya 49
>>> a // b
49
>>> #Karena "//" adalah pembagian dengan pembulatan ke bawah
>>> 10 * (a-999)
1920
>>> #Karena 1191 atau nilai a dikurangi 999 adalah 1920 lalu dikalikan 10 maka hasinya 1920
>>> b ** 2
576
>>> #Karena "**" berati perpangkatan , 24 atau nilai b dipangkatkan 2 hasilnya 576
>>> a % b
15
>>> #Karena "%" berati sisa hasil bagi
>>> c = 12.5
>>> type(c)
<type 'float'>
>>> #Karena 12.5 adalah bilangan desimal
>>> a / c
95.28
>>> #Karena 1191 dibagi 12.5 adalah 95.28, bertipe float
>>> a // c
95.0
>>> #Karena "//" adalah pembagian dengan pembulatan
>>> a % c
3.5
>>> #Karena "%" adalah sisa hasil bagi
>>> c > b
False
>>> type(c > b)
<type 'bool'>
>>> #Karena data "c > b" mempunyai dua kemungkinan nilai, yaitu True dan False
>>> c > b
False
>>> #Karena memrupakan hasil perbandingan antara objek c dan b yang menghasilkan nilai boolean
>>> a > b and b > c
True
>>> #Karena dalam pengambilan keputusan yang membutuhkan banyak perbandingan ( dan setiap perbandingan merupakan nilai true dan false sehingga termasuk operator logik), karena True and True hasilnya adalah True
>>> a > 1100 or b < 10
True
>>> #Karena hasil dari a > 1100 adalah
>>> 

>>> 

>>> #Karena hasil dari a > 1100 adalah "True" hasil dari b < 10 adalah "False", dan hasil dari True "or" False adalah True
