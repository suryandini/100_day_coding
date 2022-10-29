#statement/kondisi di antaranya adalah if, else, dan elif kondisi elif digunakan untuk mengeksekusi kode jika kondisi bernilai benar True.
#jika kondisi bernilai salah False maka statement/kondisi if tidak akan di eksekusi
#contoh penggunaan if

#Kondisi if adalah kondisi yang akan di eksekusi oleh program jika bernilai benar atau True
nilai = 10
#jika kondisi benar/TRUE maka progam akan mengeksekusi perintah di bawahnya
if(nilai > 6):
    print("sepuluh lebih besar dari angka enam")#kondisi benar. di eksekusi

#jika kondisi salah/FALSE maka program tida akan mengeksekusi perintah di bawahnya
if(nilai > 20):
    print("sepuluh lebih beasr dari pada angka dua puluh")#kondisi salah. maka tidak tereksekusi 

#Kondisi if else adalah kondisi dimana jika peryataan benar True maka kode dalam if akan di eksekusi, tetapi jika bernilai salah False maka akan mengeksekusi kode di dalam else
nilai = 5
if(nilai > 8):
    print("selamat anda LULUS")
else:
    print("maaf anda Tidak LULUS")

#Kondisi elif
hari_ini = "Sabtu"
if(hari_ini == "Senin"):
    print("saya akan sekolah")
elif(hari_ini == "Selasa"):
    print("saya akan sekolah")
elif(hari_ini == "Rabu"):
    print("saya akan sekolah")
elif(hari_ini == "Kamis"):
    print("saya akan sekolah")
elif(hari_ini == "Jumat"):
    print("saya akan sekolah")
elif(hari_ini == "Sabtu"):
    print("saya akan sekolah")
elif(hari_ini == "Minggu"):
    print("saya akan libur")

#pada program di atas, jika program dijalankan maka akan mencetak string "saya akan sekolah"

