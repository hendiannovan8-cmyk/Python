"""Penggunaan if else"""

def cek(skor):
    skor = int(input("Masukkan Skor = "))
    if skor >= 80:
        print ("Sinyal BUY (Kuat)")
    elif skor >= 50 and skor <= 80:
        print ("Sinyal HOLD (sedang)")
    elif skor <= 50:
        print ("Sinyal SELL (Lemah)")


"""Tingkat Lanjut"""
def cek_sinyal(rsi, tren_naik):
  
    if rsi <= 30 and tren_naik == True:
        print ("Sinyal BUY")
    elif rsi >= 70 and tren_naik == False:
        print ("Sinyal SELL")
    else :
        print ("Sinyal HOLD")

cek_sinyal(25,True)
cek_sinyal(75, False)
cek_sinyal(50, True)

