#fungsi keanggotaan pada Set
#fungsi union (gabungan)
grup_AlumniSmk = {
    'Andini','Musdalipa','Nurlina','Hasriani'
    }
grup_AlumniSd = {
    'Andini','Nurhidayah','Maya','Aniisa'
    }
#cara pertama
print(grup_AlumniSmk | grup_AlumniSd)
#cara kedua
print(grup_AlumniSmk.union(grup_AlumniSd))

#fungsi Intersection (irisan)
grup_AlumniSmk1 = {
    'Andini','Musdalipa','Nurlina','Hasriani'
    }
grup_AlumniSd1 = {
    'Andini','Nurhidayah','Maya','Aniisa'
    }
print(grup_AlumniSmk1 & grup_AlumniSd1)#cara satu
print(grup_AlumniSmk1.intersection(grup_AlumniSd1))#cara dua

#fungsi Difference (Selisih)
grup_AlumniSmk2 = {
    'Andini','Musdalipa','Nurlina','Hasriani'
    }
grup_AlumniSd2 = {
    'Andini','Nurhidayah','Maya','Aniisa'
    }

print('\nanggota grup_AlumniSmk2 yang bukan anggota grup_AlumniSd2')
print(grup_AlumniSmk2 - grup_AlumniSd2)
print(grup_AlumniSmk2.difference(grup_AlumniSd2))

print('\ndibalik, anggota grup_AlumniSd2 yang bukan anggota grup_AlumniSmk2:')
print(grup_AlumniSd2 - grup_AlumniSmk2)
print(grup_AlumniSd2.difference(grup_AlumniSmk2))

#fungsi Symmetric Difference (yang hanya bisa menjadi anggota satu group saja )
grup_AlumniSmk3 = {'Andini','Musdalipa','Nurlina','Hasriani'}
grup_AlumniSd3 = {'Andini','Nurhidayah','Maya','Aniisa'}
print('\nanggota yang hanya ikut satu group saja:')
print(grup_AlumniSmk3.symmetric_difference(grup_AlumniSd3))





