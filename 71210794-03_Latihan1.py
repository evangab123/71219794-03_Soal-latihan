#3.1
#Bentuk lama
print("3.1")
suhu = int(input("Masukkan suhu tubuh: "))
if suhu >= 38:
    print("Anda demam")
else:
    print("Anda tidak demam")

#3.1
masukanuser = input("Masukkan suhu tubuh: ")
try:
    suhu = int(masukanuser)
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except:
    print("Masukan anda tidak valid")

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

#3.2
masukanuser = input("Masukkan suatu bilangan: ")
try:
    bilangan = int(masukanuser)
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except:
    print("Masukan anda tidak valid")
#3.3
#bentuk lama
print("3.3")
#input a, b dan c
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# secara berurutan tulis kriteria untuk a, b, dan c
if a > b and a > c:
    print("Terbesar: ", a)
elif b > a and b > c:
    print("Terbesar: ", b)
elif c > a and c > b:
    print("Terbesar: ", c)

#3.3
#input a, b dan c
usera = input("Masukkan bilangan pertama: ")
userb = input("Masukkan bilangan kedua: ")
userc = input("Masukkan bilangan ketiga: ")

# secara berurutan tulis kriteria untuk a, b, dan c
try:
    a = int(usera)
    b = int(userb)
    c = int(userc)
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except:
    print("Masukan anda tidak valid")