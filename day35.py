#menghapus item di Dictionary

Mahasiswa = {
    'nama' : 'Suryandini',
    'umur' : 18,
    'asal' : 'Mambi'
    }
del Mahasiswa ['nama']
Mahasiswa.pop ('umur')

#cara kedua
pesan_ku = {
    "isi": "Hati-hati dijalan!"
    }
isi_pesan = pesan_ku.pop('isi')

print('isi pesan :', pesan_ku.get('isi'))
print('isi pesan:', isi_pesan)

#operator keanggotaan
#kita bisa memanfaatkan operator keanggotaan untuk tipe data Dictionary pada phyton
Buah = {
    'nama' : 'Markisa'}

print('\nApakah variabel Buah memiliki key nama?')
print('nama' in Buah)

print('\nApakah variabel Buah tidak memilki key rasa?')
print('rasa' not in Buah)


