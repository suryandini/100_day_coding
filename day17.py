#menggunakan satu if, tiga elif, dan satu else.
nilai = int(input('Masukan nilai: '))
if nilai >= 90:
    print('Predikat A')
elif nilai >= 80:
    print('Predikat B')
elif nilai >= 60:
    print('Predikat C')
elif nilai >= 50:
    print('Predikat D')
else:
    print('Predikat E')

#menggunakan if semua, tanpa elif sama sekali
#if itu artinya kita membuat satu pohon percabangan
nilai = int(input('Msukan niali: '))
if nilai >=80:
    print('Predikat A')
if nilai >=75:
    print('Predikat B')
if nilai >=55:
    print('Predikat C')
if nilai >=40:
    print('Predikat D')
else:
    print('Predikat E')
            
    
