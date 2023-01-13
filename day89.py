nama = input("Masukkan nama : ") 
golongan = input("Masukkan golongan : ") 
jam_lembur = int(input("Masukkan jam lembur : "))

if golongan == "A":
    upah = 200000
elif golongan == "B" :
    upah = 120000
elif golongan == "C":
    upah = 400000
elif golongan == "D":
    upah = 500000
else : 
    print("Tidak ada golongan ") 

if jam_lembur >= 48:
    lembur = jam_lembur - 48 
    bonus = 48 * upah + lembur * 200000
else : 
    bonus = jam_lembur * upah 
print("==========================================")
print("nama : " , nama)
print("golongan : " , golongan) 
print("lama lembur(jam) : " , jam_lembur) 
print("gaji berdasarkan golongan : " , upah) 
print("Bonus : " , bonus) 



         