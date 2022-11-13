 #Set dalam bahasa pemrograman python adalah tipe data kolektif
#yang digunakan untuk menyimpan banyak nilai dalam satu variabel dengan ketentuan:
#[nilai anggota yang disimpan harus unik (tidak duplikat)
#nilai anggota yang sudah dimasukkan tidak bisa diubah lagi
#set bersifat unordered alias tidak berurut –yang artinya tidak bisa diakses dengan index.
#contoh program
# menggunakan kurung kurawal
himpunan_siswa = {'Huda', 'Lendis', 'Wahid', 'Basith'}
print(himpunan_siswa)

# mengkonversi list ke dalam set
himpunan_buah = set(['mangga', 'apel'])
print(himpunan_buah)

# set dengan tipe data yang berbeda-beda
set_campuran = {'manusia', 'hewan', 5, True, ('A', 'B')}
print(set_campuran)

#Set bersifat unchangable
# anggota set harus dari tipe data yang immutable
set_buah = { 'mangga', 'lemon', 'alpukat', True, 1, 2, 3 }
papan_ketik = {
  (1, 2, 3),
  (4, 5, 6),
  (7, 8, 9),
  (0)
}

#Tidak bisa menerima nilai duplikat
kata_unik = {
  'sore', 'ini', 'adalah', 'sore', 'yang',
  'sangat', 'mendung'
}

print(kata_unik)
