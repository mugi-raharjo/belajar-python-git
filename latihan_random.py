import random

angka_rahasia = random.randint(1, 5)
tebakan = int(input("Masukan angka 1-5: "))

if tebakan == angka_rahasia:
    print("Tebakan benar!")
else:
    print("Tebakan salah!")
    print("Angka rahasianya adalah", angka_rahasia)