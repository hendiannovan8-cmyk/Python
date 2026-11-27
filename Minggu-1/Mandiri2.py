print("===Nilai Ujian===")
nilai = int(input("Masukkan Nilai = "))
if nilai >=85 and nilai == 100 :
    print ("Predikat: A (Sangat Memuaskan)")
elif nilai >= 75 and nilai <= 84 :
    print ("Predikat: B (Memuaskan)")
elif nilai >= 60 and nilai <= 74 :
    print ("Predikat: C (Cukup)")
elif nilai < 60 :
    print ("Pringkat: D (Kurang Baik)")
else :
    print ("Nilai Tidak Valid")