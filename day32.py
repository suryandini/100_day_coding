#cara mengakses item pada Dictionary
#dengan menggunakan kurung siku dan menggunakan fungsi get()
pertemuan_pertama = {
    "judul": "Belajar tentang Dictionary pada phyton 2", "tanggal": "16 November 2022",
                     "kategori": [
                         "phyton","phyton dasar"
                         ],
                     "page_views": 12,
                     "published": True,
                     "share_count": {
                     "facebook": 3,
                     "twitter": 1
                     }
                    }
print('judul:',pertemuan_pertama.get('judul'))
print('tanggal:', pertemuan_pertama['tanggal'])
#bisa mengguanakan fungsi berantai untuk dictionary bertingkat
print('facebook share:', pertemuan_pertama .get('share_count').get('facebook'))
#bisa juga dengan kurung siku kedua-duanya
print('twitter share:', pertemuan_pertama['share_count']['twitter'])
print('published:', pertemuan_pertama['published'])
