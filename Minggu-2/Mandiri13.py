"""Mengenal set dict tuplr dan list comprehension"""
# 3. Contoh Dict (Berisi Key dan value ditulis secara runtut ke bawah) biasanya teriri dari 2 data (duplikat)
def injektif_dict():
    # fungsi berisi Key dan Value ditulis didalam kurawal {} dan menggunakan (:) 
    fungsi_dict = {
        1: 'a',
        2: 'b',
        3: 'c'
    }
    print ("Value dari Key 1: ", fungsi_dict[1])
    print ("Value dari Key 3:", fungsi_dict[3])
    print ("Semua Keys :", fungsi_dict.keys())
    print ("Semua Values :", fungsi_dict.values())

injektif_dict()

# 1. Contoh SET (Menggunakan kurung kurawal {}, data unik/tidak ada duplikat)
def contoh_set():
    # Himpunan data angka (misalnya data domain)
    data_set = {1, 2, 3, 3, 2}  # Angka kembar akan otomatis disaring oleh set
    print("Isi Set:", data_set)  # Output: {1, 2, 3}


# 2. Contoh TUPLE (Menggunakan kurung biasa (), data statis/tidak bisa diubah)
def contoh_tuple():
    # Menyimpan data pasangan koordinat atau fungsi tetap
    data_tuple = (10, 20, 30)
    print("Isi Tuple:", data_tuple)
    print("Mengambil elemen pertama dari tuple:", data_tuple[0])  # Output: 10
    
    # Perhatikan: data_tuple[0] = 99  <-- Kalau ini dijalankan, Python akan ERROR 
    # karena isi tuple tidak boleh diubah setelah dibuat.


# Contoh Rekursi (memanggil dirinya sendiri)
def faktorial(n):
    # Titik berhenti (base case)
    if n == 1:
        return 1
    # Memanggil dirinya sendiri
    else:
        return n * faktorial(n - 1)

print(faktorial(6))  # Output: 120 (5 * 4 * 3 * 2 * 1)