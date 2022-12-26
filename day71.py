class Kucing:
    def __init__(self,warna,usia):
        self.warna = warna
        self.usia = usia



    def perkenalan(self):
      
       print(f'Saya memiliki kucing berwarna{self.kucing.warna} usia {self.kucing.usia}')

    deni = Kucing(
        kucing = Kucing(
            warna = 'Merah',
            usia = '3 bulan'
         )
    )
    deni.perkenalan()

