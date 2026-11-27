def injektif():
    fungsi = {(1, 'a'), (2, 'b'), (3, 'a')}
    for (x1, y1) in fungsi:
        for (x2, y2) in fungsi:
             if (y1 == y2) and (x1 != x2):
                 return False
    return True
print(injektif())

def surjektif():
    domain = {(1, 'x'), (2, 'y')}
    kodomain = {'x', 'y', 'z'}
    wadah = set()
    for (a, b) in domain:
        wadah.add(b)
    for z in kodomain:
            if z not in wadah:
                return False
    return True
print (surjektif())

"""Lanjut"""

#Gabungan Injektf dan Surjketif : (tidak boleh ada y1 == y2 dan x1 != x2) dan (mengambil data b untuk mengecek kodomain yang tidak terdata di domain)
def biektif():
     fungsi_data = {(1, 'p'), (2, 'q'), (3, 'r')}
     kodomain_target = {'p', 'q', 'r'}
     wadah = set()

     for (x1, y1) in fungsi_data:
          for (x2, y2) in fungsi_data:
            if (y1 == y2) and (x1 != x2):
             return False
            
            for (a, b) in fungsi_data:
                wadah.add(b)
            for z in kodomain_target:
                if z not in wadah:
                    return False
                
     return True
print (biektif())
         
          
       
