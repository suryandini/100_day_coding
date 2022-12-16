#OOP Constructor_init_()
class Barang :

    def __init__(self, inputName, inputHarga, inputWarna, inputMerek):
        self.name =  inputName
        self.harga = inputHarga
        self.warna = inputWarna
        self.merek = inputMerek

#Pembuatan objek
barang1 = Barang("Sepatu", 2.00000, "hitam","Start")
barang2 = Barang("tas",5000000, "kuning", "Gucci")
barang3 = Barang("Laptop", 8000000, "silver","Asus")

print(barang1.__dict__)
print(barang2.__dict__)
print(barang3.__dict__)
 

