#3.2
#Bentuk lama
print("3.2")
bilangan = int(input("Masukkan suatu bilangan: "))
if bilangan > 0:
    print("Positif")
elif bilangan < 0:
    print("Negatif")
elif bilangan == 0:
    print("Nol")

#Bentuk baru
bilangan = int(input("Masukkan suatu bilangan: "))

print("Positif" if bilangan > 0 else "Negatif"
    if bilangan < 0 else "Nol")