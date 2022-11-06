#perulangan while
i = 1
while i <= 18:
    print(i)
    i+=1
    

#perulangan while untuk list
    listmakanan = ['nasi_goreng','nasi_padang','gado_gado','bubur_ayam']
i = 0
while i<len(listmakanan):
    print(listmakanan[i])
    i+= 1
    

#Perintah continue berfungsi untuk men-skip iterasi sekarang ke iterasi selanjutnya.

listKota = ['Makassar', 'Jeneponto', 'Polewali', 'Majene', 'Kendari','Kalimantan']
# skip jika i adalah bilangan genap
# dan i lebih dari 0
i = -1
while i < len(listKota):
  i += 1
  if i % 2 == 0 and i > 0:
    print('skip')
    continue

  # tidak dieksekusi ketika continue dipanggil
  print(listKota[i])


