#While else
listmerek_jilbab = [
    'Rabbani','Bella square','Zoya','Elzatta','Diaro',
    'jilbab Nafisah','jilbab shasmira']
jilbab_yang_dicari = input("Masukan nama yang di cari:")

i = 0
while i < len(listmerek_jilbab):
    if listmerek_jilbab[i].lower() == jilbab_yang_dicari.lower():
        print('ketemu di index',i)
        break
    print('bukan',listmerek_jilbab[i])
    i += 1
else:
     print('Maaf,jilbab yang anda cari tidak di temukan')
     

#perulangan while dengan inputan
     a = int(input('Masukan bilangan ganjil lebih dari 50:'))
     while a % 2 != 1 or a <= 50:
         a = int(input('salah, masukan lagi:'))
     print('benar')
