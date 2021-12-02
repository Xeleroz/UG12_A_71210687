nama_orang = []
nomer_kursi = []

while (True):
    Name = str(input("Masukkan nama: "))
    if Name == "STOP":
        break
    Bangku = int(input("Masukkan nomor kursi " + Name + ": "))

    if Bangku in nomer_kursi:
        print("Mohon maaf kursi tersebut telah terisi!")
    else:
        nama_orang.append(Name)
        nomer_kursi.append(Bangku)

print()
print("List kursi yang telah terisi : ")

for a in range(0, len(nomer_kursi), 1):
    print("Kursi nomor", nomer_kursi[a], "telah diisi oleh", nama_orang[a])