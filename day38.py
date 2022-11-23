#fungsi dan parameter
def selamat_datang (Mahasiswa):
    print(f'apakabar {Mahasiswa}, sekarang kamu kuliah dimana dan kamu ambil jurusan apa?')

selamat_datang('Suryandini')
selamat_datang('Musdalifa')
selamat_datang('Fitrah')
selamat_datang('Nurlaelia')
print("====================================================")

#parameter wajib
#parameter di dalam phyton bisa lebih dari satu, bisa wajib semua (harus diisi), dan
#bisa juga bersifat opsional

def perkenalan (nama, asal, Hobi):
    print(f" perkenalkan nama saya {nama} saya berasal dari kota {asal} hobi saya bermain {Hobi}")

perkenalan("Suryandini","Mambi","Bulu tangkis")

#parameter opsional (default)
def suhu_udara(daerah, derajat, satuan = 'scelcius'):
    print(f"suhu di {daerah} adalah {derajat} {satuan}")
    
suhu_udara("Jakarta", 40)
suhu_udara("Jakarta", 67, 'Farenheit')
suhu_udara("kalimantan", 55)
