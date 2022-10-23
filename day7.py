#Tentang tipe data pada phyton
#Tipe 1 : Tipe data karakter
#* menyatakan karakter atau sekumpulan karakter atau seringkali di sebut string
#* Tipe data string bisa berupa huruf atau angka
#* Nilai karakter harus diapit tanda " atau '.
#contoh
nama = "suryandini"
alamat = 'Mambi'
umur = "18thn"
print ("umur",umur)

#Tipe data 2 : Tipe Data numerik
# * Tipe data integer : menyatakan bilangan bulat
# * Tipe data float: menyatakan nilai pecahan desimal
# * Oktal(bilangan berbasis 8).
jari_jari = 40
phi = 3.14
angka = 6776
print ("Luas lingkaran = ", phi*jari_jari*jari_jari)

#Tipe data 3 : Boolean
#Tipe data yang menyatakan jika benar bernilai True atau 1, atau jika salah bernilai false atau 0
Lulus = True
gagal = False
print ("Lulus =",Lulus)
print ("gagal =",gagal)

#Tipe data list
#adalah tipe data untaian, yaitu struktur data yang mampu menyimpan lebih dari satu data
#dengan berbagai tipe data. List dibuat seperti halnya variabel biasa, tetapi nilai variabelnya diisi
#dengan tanda kurung ("[]")
#contoh
#membuat List kosong
buah = []
#membuat isi List
buah =["Apel","Anggur","Jambu","pisang"]
print ("buah = ", buah [0]) #memanggil index dari buah
print ("buah = ", buah [1])
print ("buah = ", buah [2])
print ("buah = ", buah [3])

#Tipe data Tuple
#Merupakan tipe data untaian yang juga menyimpan berbagai tipe data, tetapi bersifat immutable,
# artinya isinya tidak bisa dirubah. Tuple bisa dibuat di dalam sebuah tanda kurung, atau bisa juga tidak.
#Contoh:
# Dengan tanda kurung
nilai1 = (80, 90, 'lulus')
#Tanpa tanda kurung
nilai2 = 80, 90, 'lulus'
print ("Nilai 1 =", nilai1[2])#memanggil index
print ("Nilai 2 =", nilai2[1])










