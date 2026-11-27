"""Terjemahkan Pernytaan Logika ke Python"""

def konjungsi(p, q):
    return p and q
print (konjungsi(True, True))

def disjungsi(p, q):
    return p or q
print(disjungsi(True, True))

def negasi(p):
    return not p
print (negasi(True))

def implikasi(p, q):
    return (not p) or q
print (implikasi (True, True))

def biimplikasi(p,q):
    return p == q
print (biimplikasi(True, True))

def DeMorgan1(p,q):
    kanan = not (p and q)   
    kiri = (not p) or (not q)
    return kanan == kiri
print (DeMorgan1(True, True))

def DeMorgan2(p, q):
    kanan = not (p or q)
    kiri = (not p) and (not q)
    return kanan == kiri
print (DeMorgan2(True, True))

"""Tingkat Lanjut"""

def latihan1(p, q, r):
    return not (p and q) or (not r)
print(latihan1(True, True,False))

def latihan2(p, q, r):
    return not (p or q) and r
print (latihan2(True, True, True))

def latihan3():
    kombinasi = [True, False]
    for p in kombinasi:
        for q in kombinasi:
            for r in kombinasi:
                    kanan = not (p or q) and r
                    kiri = (not p and not q) and r
                    print (f"p{p}, q{q}, r{r} hasil: {kanan == kiri}")              
               
latihan3()
