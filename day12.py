#Program Aritmatika
#Mencari luas segitiga
#pada program ini menggunakan fungsi input untuk mendapatkan nilai pada variabel alas dan tinggi
#yang dimana rumus dari mencari luas segitiga
#dengan begitu untuk menemukan luas segitiga di perlukan nilai dari alas dan tinggi kemudian di kalikan nilai 1/2.
alas = int(input("masukan alas segitiga ="))
tinggi = int(input("masukan tinggi segitiga ="))
seperdua=(1/2)
luas=(seperdua*alas*tinggi)
print("luas segitiga =",luas, "cm2")

#Menghitung luas lingkaran
phie = (3.14)
r = int(input("masukkan nilai jari-jari ="))
luas = (phie*r*r)
print("luas lingkaran =", luas, "cm")

for suku in range(1, 100, 5):
 print(suku)

hasil= 0
for suku  in range(1, 100, 5):
    hasil = hasil + suku
    print(suku)
print("sn = {}".format(hasil))



