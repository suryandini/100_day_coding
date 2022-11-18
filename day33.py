#perulangan untuk Dictionary
#contoh
Alquran = {
     'nama_surah': 'Al_Mulk','memiliki arti': 'Kerajaan', 'surah_ke': '67 dalam_Alquran','surah_ini':'tergolong Makkiyah',
     'surah_ini_terdiri_dari': '30 ayat'}

for key in Alquran:
    print(key, '->', Alquran[key])

print("============================================================")

#kita juga bisa memanggil fungsi dictionary.items() untuk perulangan 
#contoh
Alquran = {
     'nama_surah': 'Al_Mulk','memiliki arti': 'Kerajaan', 'surah_ke': '67 dalam_Alquran','surah_ini':'tergolong Makkiyah',
     'surah_ini_terdiri_dari': '30_ayat'}

for nama_atribut, nilai in Alquran.items():
    print(nama_atribut, '->', nilai)
