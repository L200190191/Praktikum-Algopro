import shelve

file = open("L200190191.txt", "r")
NIM = file.readline()
Tanggal = file.readline()
Nama = file.readline()
Kota = file.readline()
Ttl = Kota + Tanggal
file.close()

F = shelve.open("Kurnia.txt")
F["data"] = [Nama, NIM, Ttl]

print(F["data"][0])
print(F["data"][1])
print(F["data"][2])
