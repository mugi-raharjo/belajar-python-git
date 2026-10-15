nama = "Mugi"
usia = 25
kota = "Jakarta"

with open("profil.txt", "w") as file:
    file.write("Nama: " + nama + "\n")
    file.write("Usia: " + str(usia) + "\n")
    file.write("Kota: " + kota)

with open("profil.txt", "r") as file:
    isi = file.read()

print(isi)