class Kendaraan:
    def berjalan(self):
        print('berjalan..')

class Mobil(Kendaraan):
    def berjalan(self,kecepatan, satuan = 'km/j'):
        print(f'mobil ini  bisa Berjalan dengan kecepatan {kecepatan} {satuan}')

motor = Kendaraan()
barang = Mobil()

motor.berjalan()
barang.berjalan(140)
