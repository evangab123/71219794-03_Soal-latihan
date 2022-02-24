print("=====Program untuk tahu jumlah hari pada Suatu Bulan=====")
masukanuser = input("Masukan bulan keberapa?(1-12)= ")
try:
    bulan= int(masukanuser)
    if (bulan%2 == 1 and 0<bulan<=7) or (bulan%2 ==0 and 13>bulan>7):
        print("Jumlah harinya adalah 31!")
    elif bulan == 2:
        print("Jumlah harinya adalah 28 dan juga 29")
    elif bulan<=0 or bulan>12:
        print("tidak ada bulan ke", bulan)
    else :
        print("Jumlah harinya adalah 30")
    
except:
    print("Bulan yang anda inputkan tidak valid!")