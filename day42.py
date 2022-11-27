for i in range(15):
    print(i)
print("=======================================================")

#Fungsi Rekursif
#merupakan sebuah metode perulangan yang bersifat non iterasi
def tampilkanAngka (batas, i = 1):
        print(f'perulangan ke {i}')

        if (i < batas):
            #disinilah rekursifitas itu terjadi
            tampilkanAngka(batas, i + 1)
#memanggil fungsi tampilanAngka untuk pertama kali
tampilkanAngka(10)

print("========================================================")

#membalik perintah print() dan perintah rekursif. yang awalnya print() terlebih dulu
#kemudian proses rekursif, sekarang kita ubah menjadi proses rekursif dahulu baru setelah itu proses print()

def tampilkanAngka (batas, i = 1):
    if (i < batas):
        tampilkanAngka (batas, i + 1)
    print(f'perulangan ke {i}')

tampilkanAngka(10)
            
    
