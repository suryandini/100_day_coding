#for dengan tuple
tupleWarna = ('hitam','coklat','putih','biru')
for warna in tupleWarna:
    print(warna)

#for dengan string
for karakter in 'indonesia':
    print(karakter)

#break dan continue
for i in range(10,20):
    #skip jika i == 12
    if(i == 10):
        continue
    print(i)

for i in range(20,35):
    #hentikan jika i == 26
    if(i == 35):
        break
    print(i)
    
