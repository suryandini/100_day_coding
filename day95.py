class Mahasiswa:
  # static atau class variable
  jenjang = 'S2'

  def __init__(self, nama):
    # instance variable
    self.nama = nama

ahmad = Mahasiswa('Ahmad')
print(ahmad.jenjang)

arya = Mahasiswa('Arya')
print(arya.jenjang)

Mahasiswa.jenjang = 'SMA'

print(ahmad.jenjang)
print(arya.jenjang)