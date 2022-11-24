#fungsi yang mempunyai atau mengembalikan nilai
def luas_persegi (sisi):
    return sisi*sisi #return ini untuk mengembalikan nilai
luas_persegi(12)
print('luas persegi dengan sisi 4 adalah:',luas_persegi(4))

persegi_besar = luas_persegi(120)
persegi_kecil = luas_persegi(30)

print('Total luas persegi besar dan kecil adalah:', persegi_besar + persegi_kecil)

#contoh lebih dari satu return
def persentase (total, jumlah):
    if (total >= 0 and total <= jumlah):
        return total / jumlah * 100
    return False
print(persentase(80,65))
print(persentase(120,75))

#Ruang lingkup (dan siklus hidup) variabel pada fungsi
#variabel global
#adalah variabel  yang bisa di panggil dari manapun dari file phyton
#variabel lokal
#adalah variabel yang hanya hidup di dalam satu blok kode tertentu (seperti di dalam fungsi)

Buah = 'Melon'

def manisnya():
    print(Buah)

print('print secara langsung enaknya buah', Buah)
print('[panggil fungsi manisnya buah]', end=' ')
manisnya()
print("===================================================")

kota, provinsi = 'Sulbar', 'sulsel'
def hello ():
    provinsi = 'Sulbar'
    print(kota, provinsi)
    
print('[PANGGIL FUNGSI hello()]')
hello()
print('\n[SECARA LANGSUNG]')
print(kota, provinsi)


