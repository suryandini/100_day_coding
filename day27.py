for i in range(5):
    print("perulangan di luar [i] = ",i)

    for j in range (7):
          print('perulangan di dalam =',str(i)+','+str(j))

#tambahan perulangan bersarang menggunakan while
max_baris = 6
max_kolom =8
baris = 0
while baris < max_baris:
     kolom = 0
     while kolom < max_kolom:
       print('0' if kolom <= baris else '+', end = ' ')
       kolom += 1
     else:
       print('')
     baris += 1

