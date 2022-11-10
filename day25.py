#Perulangan bersarang atau perulangan bertingkat adalah sebuah perulangan
#yang berada atau terletak di dalam perulangan yang lain.
for i in range(3):
  print('Perulangan luar [i] = ', i)

  for j in range(5):
    print('   Perulangan dalam [i, j] = ', str(i) + ', ' + str(j))

for baris in range(5):
  for kolom in range(7):
    print('o', end = ' ')
  else:
    print('')

listBuah = [
  'Apel', 'Anggur', 'Pisang'
]

for Buah in listBuah:
  print(Buah)
  
  listTempat = [
    'indomaret', 'pasar', 'Mall'
  ]

  while listTempat:
    print('-->', listTempat.pop(0))
