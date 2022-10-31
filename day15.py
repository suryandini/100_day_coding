kurus = float(input("Masukan kurus anda : "))
kbb = float(input("Masukan kelebihan berat badan anda : "))
normal = float(input("Masukan normal berat anda : "))
gemuk_kbb = float(input("Masukan kelebihan berat anda : "))
gemuk = int(input("Masukan gemuk anda : "))

if kurus == 18.0:
    print("kekurangan berat badan ringan !!",kurus)
elif kbb == 18.0 <=19.5:
    print("kurus, kekurangan berat badan..!!",kbb)
elif kbb == 19.5 <=20.1:
    print("berat badan Normal..!!",normal)
elif kbb == 20.1 <=25.5:
    print("gemuk, kelebihan berat badan tingkat ringan..!!",gemuk_kbb)
elif kbb == 25:
    print("Gemuk, kelebihan berat badan tingkat berat..!!",gemuk)
else :
    clear

