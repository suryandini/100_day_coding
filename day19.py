#Pada python, kita bisa menggunakan if..else dalam satu baris.
#Biasanya, pada bahasa pemrograman lainnya, ini disebut sebagai ternary (meskipun python cukup unik dari segi sintaksisnya).
#Perhatikan contoh berikut:

nilai = int(input('Masukkan nilai: '))
status = 'lulus' if nilai >= 70 else 'tidak lulus'

print(status)

#kode program di atas adalah shorcut dari kode seperti berikut:
if nilai >= 80:
    status = 'Lulus'
else:
    status = 'Tidak Lulus'

print(status)

#Percabangan Bertingkat (sebuah istilah untuk if di dalam if.

nilai = int(input('Masukan nilai: '))
usia = int(input('Masukkan usia: '))

if nilai >= 75:
  if (usia < 15):
    print('Selamat adek, kamu lulus!')
  else:
    print('Selamat kakak, kamu lulus!')
else:
  if (usia < 15):
    print('Mohon maaf dek, coba lagi ya!')
  else:
    print('Mohon maaf kak, coba lagi ya!')

#Kode program di atas akan memeriksa terlebih dahulu apakah nilai yang dimasukkan adalah lulus atau tidak.
#Setelah itu, program akan memeriksa usia, apakah dia akan disapa dengan “kakak” atau kah dengan “adek”.
