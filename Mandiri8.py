"""Verifikasi Hukum DeMorgan dengan True False"""

def DeMorgan1():
    for p in [True, False]:
        for q in [True, False]:
            kanan = not (p and q)
            kiri = (not p) or (not q)
            print (f"p{p}, q{q}, hasil: {kanan == kiri}")
DeMorgan1()

def DeMorgan2():
    for p in [True, False]:
        for q in [True, False]:

            kiri = not (p or q)
            kanan = (not p) and (not q)
            print (f"p{p}, q{q}, hasil: {kanan == kiri}")
DeMorgan2()

        
"""Tingkat Lanjut"""

def DeMorgan1():
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                for s in [True, False]:
                    kanan = not (p and q and r and s)
                    kiri = (not p) or (not q) or (not r) or (not s)
                    print(f"p{p}, q{q}, r{r}, s{s}, hasil: {kanan == kiri}")
DeMorgan1()

