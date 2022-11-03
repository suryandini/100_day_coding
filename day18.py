#pada percabangan if else, operator logika dan juga tipe data boolean
#berikut contohnya untuk operator keanggotaannya:
buah_yang_tersedia = ['jeruk', 'mangga', 'melon']
buah_yang_dicari = input('Masukan nama buah dalam huruf kecil: ')

if(buah_yang_dicari in buah_yang_tersedia):
 print('Buah yang anda cari tersedia!')
else:
    print('Buah yang anda cari tidak tersedia!')

#pada phyton, kita bisa mengguanakan if else dalam satu baris. Biasanya, pada bahasa pemprograman lainnya,
#ini di sebut sebagai ternary (meskipun phyton cukup unik dari segi sintaksisnya).
#Perhatikan contoh berikut:
nilai = int(input('Masukan nilai : '))
status = 'lulus' if nilai >= 70 else 'tidak lulus'

print(status)

#kode program diatas adalah shorcut dari kode seperti contoh di bawah:
if nilai >= 60:
    status = 'lulus'
else:
    status = 'tidak lulus'

print(status)
