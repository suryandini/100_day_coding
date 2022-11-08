#perulangan while dengan break
#Kita juga bisa menggunakan perintah break pada perulangan while.
#Perintah break itu sebenarnya mirip dengan perintah continue. Bedanya
#Ketika perintah break dipanggil, maka perulangan akan dihentikan secara paksa

listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

kotaYangDicari = input('Masukkan nama kota yang dicari: ')

i = 0
while i < len(listKota):
  if listKota[i].lower() == kotaYangDicari.lower():
    print('Ketemu di index', i)
    break

  print('Bukan', listKota[i])
  i += 1
