kembali = "y" or "Y"
while kembali == "y" or "Y":
    print("")
    print(" NAMA NAMA SURAH DALAM AL QURAN  ")
    print("==========================================")
    print("\t\ 10 NAMA SURAH DI JUZ 30\t ")
    print("|=========================================|")
    print(" ")
    print(" 1. An-Naba ")
    print(" 2. An-Naziat")
    print(" 3. Abasa")
    print(" 4. At-Takwir")
    print(" 5. Al-Infitar")
    print(" 6. Al- Mutaffififin")
    print(" 7. Al-insyiqaq")
    print(" 8. Al-Buruj")
    print(" 9. At-Tariq")
    print(" 10. Al-Ala ")
    print(" ")
    
    pilih = int(input("Silahkan pilih nama surah yang anda inginkan:"))

    if pilih == 1:
        nama_surah = "An-Naba"
        juz = 30
        memiliki_arti = "Berita besar"
        surah = "makkiyah"

    elif pilih == 2:
        nama_surah = "An-Naziat"
        juz = 30
        memiliki_arti = "Malaikat malaikat yang mencabut"
        surah = "makkiyah"

    elif pilih == 3:
        nama_surah = "Abasa"
        juz = 30
        memiliki_arti = "ia bermuka masam"
        surah = "makkiyah"

    elif pilih == 4:
        nama_surah = "At-Takwir"
        juz = 30
        memiliki_arti ="menggulung"
        surah = "makkiyah"

    elif pilih == 5:
        nama_surah = "Al-Infitar"
        juz = 30
        memiliki_arti ="terbelah"
        surah = "Makkiyah"

    elif pilih == 6:
        nama_surah = "Al- Mutaffififin"
        juz = 30
        memiliki_arti ="orang-orang yang curang"
        surah = "Makkiyah"
        

    elif pilih == 7:
        nama_surah = " Al-insyiqaq"
        juz = 30
        memiliki_arti ="terbelah"
        surah = "Makkiyah"

    elif pilih == 8:
        nama_surah = "Al-Buruj"
        juz = 30
        memiliki_arti ="gugusan bintang"
        surah = "Makkiyah"

    elif pilih == 9:
        nama_surah = "At-Tariq"
        juz = 30
        memiliki_arti ="yang datang di malam hari"
        surah = "Makkiyah"
        
    elif pilih == 10:
        nama_surah = "Al-Ala"
        juz = 30
        memiliki_arti ="yang paling tinggi"
        surah = "Makkiyah"

    else:
        
      print("")
      kembali=input('lagu tidak tersedia,silahkan masukkan nama surah yang tersedia ulangi kembali y/n : ')
      
    print("============================SURAH YANG DI PILIH=============================")
    print("============================================================================")
    print("NAMA SURAH         :" , nama_surah) 
    print("JUZ                : " , juz) 
    print("MEMILIKI ARTI      : " , memiliki_arti) 
    print("SURAH              : " , surah)  
    print("\n\n========================================================================\n\n")
    kembali=input('ketik y dan n untuk program selanjutnya  : ') 
    print("\n\n========================================================================\n\n") 


    # Terimakasih banyak mentor Padly atas 100 harinya :)

    h =0
    while h <= 100:
     print("Terimakasih mentor Padly :)",h) 
     h+=1 
