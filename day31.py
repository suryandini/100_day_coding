#Struktur Dictionary
#Dictionary adalah tipe data pada python yang berfungsi untuk
#menyimpan kumpulan data/nilai dengan pendekatan “key-value”.
#Perhatikan contoh di atas, variabel pertemuan_hari_ini adalah dictionary

pertemuan_pertama = {"judul": "Belajar tentang Dictionary pada phyton", "tanggal": "16 November 2022",
                     "kategori": [
                         "phyton","phyton dasar"
                         ],
                     "page_views": 12,
                     "published": True,
                     "share_count": {
                     "facebook": 5,
                     "twitter": 3
                     }
                    }
#Ia memiliki 6 buah “key” atau “atribut”, yaitu:
#judul
#tanggal
#kategori
#page_views
#published
#dan share_count (bahkan value dari share_count sendiri adalah sebuah dictionary

#Sifat Dictionary Items
#Dictionary items memiliki 3 sifat, yaitu:
#Unordered - tidak berurutan
#Changeable - bisa diubah
#Unique - alias tidak bisa menerima dua keys yang sama
#contoh
artikel = {
  "judul": "Matkul hari senin",
  "judul": "matkul yang masuk hari senin di kelas G teknik informatika"
}
print(artikel.get("judul"))

#cara membuat dictionary
# cara satu
buku = {
  "kata_kata": "Jadilah seperti mata air yang jernih. yang dapat memberi manfaat kepada manusia lainnya",
  "motivator": "Bj Habibie"
}

# cara dua
buku = dict(
  kata_kata ="Jadilah seperti mata air yang jernih. yang dapat memberi manfaat kepada manusia lainnya",
  motivator ="Bj Habibie"
)

                     
