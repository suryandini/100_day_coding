total_belanja =int(input("total belanja : Rp ")) 

bayar = total_belanja 

if total_belanja > 200000: 
    print("kamu mendapatkan minuman dingin") 
    print("kamu juga mendapatkan dison 4%") 

    diskon = total_belanja * 2/200 
    bayar = total_belanja - diskon 
    

print("Total yang harus di bayar : Rp %s" % bayar) 
print("Terimaksih") 
print("Datang lagi yah ")  