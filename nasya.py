print("============== MENU ==============")
print("1. Konversi Suhu")
print("2. Bangun Ruang")
pilih = input("Silahkan pilih menu dibawah 1/2 : ")
if(pilih == "1"):
    celcius = int(input("Silahkan masukkan suhu Celcius : "))
    fahrenheit = (5/9)*celcius +32
    reamur = (4/5)*celcius
    print("Hasil Konversi Suhu :")
    print("Fahrenheit : ", fahrenheit, "F")
    print("Reamur : ", reamur, "R")
elif(pilih == "2"):
    sisi = int(input("Silahkan masukkan panjang sisi : "))
    luasKubus = sisi*sisi*sisi
    print("Luas Kubus = ", luasKubus)
else:
    print("Menu yang dipilih tidak tersedia")