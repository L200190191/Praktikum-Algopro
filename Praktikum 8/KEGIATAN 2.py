file = open("L200190191.txt", "w")
file.write("L200190191\n")
file.write("11/20/2000\n")
file.write("Kurnia Indah Nur Cahyani\n")
file.write("Karanganyar,")
file.close()

file = open("L200190191.txt", "r")
NIM = file.readline()
Tanggal = file.readline()
Nama = file.readline()
Kota = file.readline()
TTL = Kota + Tanggal
print(Nama)
print(TTL)
print(NIM)
file.close()
