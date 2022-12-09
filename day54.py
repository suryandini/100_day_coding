investasi=100
bunga=10/100
keuntungan=0
tahun=0

while keuntungan < 1000:
      keuntunganpertahun = investasi * bunga
      keuntungan += keuntunganpertahun
      print("jumlah investasi adalah:",investasi)
      investasi +=keuntunganpertahun
      tahun+=1
      print("keuntungan tahun ke:",tahun,"adalah",keuntungan)
      print(20*"=")


nilai=int(input("masukkan nilai:"))
if nilai >=88:
    print("A")
elif nilai >=77:
    print("B")
elif nilai >=60:
    print("C")
elif nilai >=45:
    print("D")
else:
    print("E")
    
x=(int(input("bialangan bulat sembarang:")))
if x != 0:
     nilai_fungsi=(int(2*x**3+2*x+15/x))
     print("niali fungsi:", nilai_fungsi)
elif x == 10/100:
    print("x yang anda masukkan nilai desimal")
else :
    print("anda memasukan nilai x dengan bilangan caca")

def tampil (batas, i=100):
    print(i)
    if i < batas:
            tampil (batas,i*10/100+i)
tampil(1000)
