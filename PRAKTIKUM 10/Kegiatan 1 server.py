import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50001))
s.listen(5)
print "Program Komunikasi Tentang Data Diri"
data = ""
kamus = {"nama":Kurnia Indah Nur Cahyani",
         "NIM":"L200190191",
         "Angkatan":"2019",
         "keluar":"Siap!"}
while data.lower() != "keluar":
    komm, addr = s.accepr()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print "Perintah: ", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Maaf, Perintah Tidak Dimengerti")
