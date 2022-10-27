Barang = ['sepatu','tas','buku','pulpen']
print(Barang)

#Beberapa method yang bisa digunakan untuk memanipulasi list
#Method untuk menambah data ke dalam list
Barang.append('kursi') # untuk menambah data ke dalam list
print(Barang)

Barang.extend('baju') # dia akan mengambil intrabelsnya disini
print(Barang)

Barang.insert(4,'celana')# untuk menambah data di tengah sesuai indeks yang di masukkan
print(Barang)

#menghapus data
Barang.remove('tas')
print(Barang)

Barang.reverse()
print(Barang)

Stuff = Barang.copy()
Stuff.append('sendok')
print(Stuff)
print(Barang)

