#tipe data sets (sebuah colection yang tidak mempunyai index)dia hanya kumpulan data atau himpunan
#dimana tidak ada urutannya
#menggunakan kurung kurawal
data_sets = {20,12,11,10,2,3,4}
print(data_sets)

#print{data_sets[0]) dia tidak terbaca karena dimana dia tidak mempunyai index

#list (array, mengakses dengan menggunakan index
data_list = ['Alya', 'Dini', 'Laelia']
print(data_list[0])

#tipe data dictionary
# dictionary (dict) ossosiative array
# identifier/ identitas (key)
data_dict = {
    'key' : 'value1', #(bentuk dari dictionary
    'key' : 'value2'
}
print(data_dict)

data_dict = {
    'al' : 'alya',      # ini berguna jika kita membutuhkan sebuah data yang mempunyai struktur
    'dn' : 'dini',
    'nd' : 'nanda',
    'ip' : 'ipa',
    'nmor' : 10,
    'list' : data_list,
}

print(data_dict['dn'])
print(data_dict['nd'])
print(data_dict['ip'])
print(data_dict['nmor'])
print(data_dict['list'])




