class Mobil:
  def __init__(self, tahun):
    self.tahun = tahun

  @property
  def tahun(self):
    return self.__tahun

  @tahun.setter
  def tahun(self, tahun):
    if tahun > 2021:
      self.__tahun = 2021
    elif tahun < 1990:
      self.__tahun = 1990
    else:
      self.__tahun = tahun

sedan = Mobil(2200)


print(f'Mobil ini dibuat tahun {sedan.tahun}')


