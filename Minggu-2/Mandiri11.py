"""Cek sifat refleksi"""

def soal1():
    himpunan_A = {1, 2, 3}
    relasi= {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
    for x in himpunan_A:
        if (x, x ) not in relasi:
         return False
    return True
print (soal1())


def soal2():
   relasi= {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
   for (a, b) in relasi:
      if (b, a) not in relasi:
       return False
   return True
print(soal2())

def soal3():
   relasi= {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
   for (a, b) in relasi:
      for (b2, c) in relasi:
         if (b2 == b):
           if (a, c) not in relasi:
            return False
   return True
print(soal3())

#Lanjut

def ekuivalen():
   return all([soal1(), soal2(), soal3()]) 
print(ekuivalen())

def antisimatris():
    relasi = {(1, 1), (2, 2), (3, 3), (1, 3), (2, 1)}
    for (a, b) in relasi:
        if (b, a) in relasi:
            if a != b:
                return False
    return True

print(antisimatris())


def ekstrasi_domain():
    relasi = {(1, 2), (1, 3), (2, 3)}
    domain_set = set()  # Membuat wadah set kosong
    for a, b in relasi:
        domain_set.add(a)  # Masukkan elemen pertama (a) ke dalam wadah
    return domain_set
print(ekstrasi_domain())