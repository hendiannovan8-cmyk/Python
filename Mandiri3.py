print("=== Status Diskon ===")
Total = int(input("Masukkan Total Beanja = "))
Status = input("Apakah anda Member? (ya/tidak) ").lower()
TotalDiskon1 = (Total * 20) / 100
TotalDiskon2 = (Total * 10) / 100
TotalDiskon3 = (Total * 5) / 100

if Status == "ya" and Total >= 100000:
    HargaAkhir = Total - TotalDiskon1
    print("Diskon 20%"and TotalDiskon1)
    print("Harga Akhir = ", HargaAkhir)

elif Status == "ya" and Total < 100000:
    HargaAkhir = Total - TotalDiskon2
    print ("Diskon 10%" and TotalDiskon2)
    print("Harga Akhir = ", HargaAkhir)

elif Status == "tidak" and Total >= 200000:
    HargaAkhir = Total - TotalDiskon3
    print("Diskon 5%" and TotalDiskon3)
    print("Harga Akhir = ", HargaAkhir)
else:
    print("Anda tidak dapat diskon")
