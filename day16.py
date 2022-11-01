print('kalkulator luas persegi panjang\n')
panjang = input('masukkan panjang: ')
lebar = input('Masukkan lebar: ')

print('Luas =', int(panjang)*int(lebar))

#dengan parameter end, kita bisa mengganti karakter ganti baris bawaan python
#dengan karakter lain sesuai keinginan kita.
print('Suryandini', end=' ')
print('Nurlaelia', end=' ')
print('Nurul inayah', end=' ')
print('Musdalifa', end=' ')

#menggunakan parameter end dan sep secara bersamaan:
print('1','2','3', sep="*", end="@")

print('1','2','3', sep="s",end="o\n")
