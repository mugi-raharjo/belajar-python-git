data = "Mugi,Budi,Andika"

data_rapih = data.split(",")

for data_baru in data_rapih:
    if len(data_baru) > 4:
        print(data_baru, "panjangnya lebih dari 4 karakter")