try:
    angka = int(input("Masukan angka: "))
    print("Angka kamu adalah:", angka)
except ValueError:
    print("Input harus berupa angka!")