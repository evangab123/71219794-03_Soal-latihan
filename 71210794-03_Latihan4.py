masukanuser1 = input("Masukan sisi 1 :")
masukanuser2 = input("Masukan sisi 2 :")
masukanuser3 = input("Masukan sisi 3 :")

try:
    sisi1 = int(masukanuser1)
    sisi2 = int(masukanuser2)
    sisi3 = int(masukanuser3)
    if sisi1 == sisi2 and sisi2 == sisi3:
        print("3 Sisi sama")
    elif (sisi1 ==sisi2 and sisi2 != sisi3) or (sisi1 != sisi2 and sisi2==sisi3) or (sisi1 == sisi3 and sisi2 != sisi1):
        print("2 sisi sama")
    else :
        print("Tidak ada yang sama")
except:
    print("Masukan anda tidak valid")