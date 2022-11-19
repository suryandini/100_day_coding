#Mengubah nilai item
#item pada Dictionary bersifat changeable alias bisa diubah.

print('Nama-nama Wanita teladan untuk kaum Hawa')
print("========================================")

Wanita_teladan = {'nama': 'Khadijah binti Khuwailid',
                   'Asal' : 'Makkah'}
 # mengubah data
print('Nama awal:',Wanita_teladan.get('nama'))
print('Asal:',Wanita_teladan.get('Asal'))
Wanita_teladan['nama'] = 'Aisyah binti Abu Bakar'
Wanita_teladan['Asal'] = 'Arab'
print('seteleh di ubah Nama:',Wanita_teladan.get('nama'))
print('seteleh di ubah Asal:',Wanita_teladan.get('Asal'))

Wanita_teladan['nama'] = 'Maryam binti imran'
Wanita_teladan['Asal'] = 'Makkah'

print('setelah di ubah Nama:',Wanita_teladan.get('nama'))
print('setelah di ubah Asal:',Wanita_teladan.get('Asal'))

 # menambahkan item
Wanita_teladan = {'nama': 'Khadijah binti Khuwailid',
                   'Asal' : 'Makkah'}
  #tambah data
Wanita_teladan['kelebihan'] = 'Bijaksana dan Cerdas'
  #print ulang
print('kelebihan dari {} adalah {}'.format(
    Wanita_teladan.get('nama'),
    Wanita_teladan.get('kelebihan')
  ))


                  
                           
