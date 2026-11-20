"""Operasi Himpunan Python"""
def himpunan1():
    himpunan_A = {"BTC", "ETH", "SOL", "ADA"}
    himpunan_B = {"SOL", "ADA", "XRP", "DOT"}

    print (f"set A: {himpunan_A.union(himpunan_B)}")
    print (f"set B: {himpunan_A.intersection(himpunan_B)}")
    print (f"set C: {himpunan_A.difference(himpunan_B)}\n")
himpunan1()

"""Tingkat Lanjut"""
def himpunan2():
    A = {"BTC", "ETH", "SOL", "ADA"}
    B = {"SOL", "ADA", "XRP", "DOT"}
    print (f"Selisih Simetris: {A.symmetric_difference(B)}")
himpunan2()

def himpunan3():
    koin_aktif = {"BTC", "ETH", "SOL", "DOGE", "SHIB"}
    blacklist = {"DOGE", "SHIB"}
    print (f"Penyaringan Blacklist: {koin_aktif.difference(blacklist)}")
himpunan3()

def himpunan4():
    portofolio_utama = {"BTC", "ETH", "SOL", "ADA", "XRP", "DOT"}
    portofolio_kecil = {"BTC", "ETH"}
    print (f"Cek Himpunan Bagian: {portofolio_kecil.issubset(portofolio_utama)}")
himpunan4()