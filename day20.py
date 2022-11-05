#Menampilkan list bilangan genap/ganjil dari range tertentu
print('Masukan nilai awal dan nilai akhir')

nilai_awal =int(input(' nilai awal: '))
nilai_akhir =int(input(' nilai akhir: '))

print("""\nTampilkan bilangan
1. Ganjil
2. Genap""")

pilihan = int(input ('pilihan: '))

#menampilkan bilangan ganjil saja jika pilihan sama dengan 1, dan menampilkan bilangan genap saja jika pilihan sama dengan 2
if pilihan not in [1, 2]:
    print('pilihan salah')
else:
    for x in range(nilai_awal, nilai_akhir + 1):
        if pilihan == 1 and x %2 == 1:
            print(x, end=' ')
        elif pilihan == 2 and x % 2 == 0:
            print(x, end=' ')
    else:
        #ganti baris ketika perulangan selesai
     print('')
              
