def persegi_panjang():
    print("Menghitung luas persegi panjang")
    panjang = int (input("masukkan nilai panjang:"))
    lebar = int(input("Masukan nilai lebar:"))
    luas = (panjang*lebar)
    print("luas persegi panjang adalah:", luas,"cm")
persegi_panjang()

print("================================================")
def Lingkaran():
    print("Menghitung luas Lingkaran")
    phi = float(input("Masukan nilai phi:"))
    r = int(input("Masukan nilai r:"))
    luas = (phi*r*r)
    print("Luas Lingkaran adalah:",luas,"cm")

Lingkaran()

print("================================================")

def segitiga():
    print("Menghitung Luas segitiga")
    alas =int(input("Masukan nilai alas:"))
    tinggi = int(input("Masukan nilai tinggi:"))
    luas = (alas*tinggi/2)
    print("luas segitiga adalah:",luas,"cm")

segitiga()
    
    
    
