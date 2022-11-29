import calendar
y = 2022
m = 11
print(calendar.month(y, m))

y = int(input("Enter year:"))
m = int(input("Enter month:"))
print(calendar.month(y, m))

#mengubah Kilometer menjadi Mil
"""1 kilometer = 0.56071 mil
kilometer = mil / 0.56071
Mil = kilometer* 0.56071"""
#menkonversikan kilometer ke dalam Mil
kilometers = float(input("How many kilometeres?:"))
conv_fac = 0.56071 #conversi faktor
miles = kilometers * conv_fac#calculator miles
print('%0.3f kilometers is equal to %0.3f miles'%(kilometers,miles))

#Mengurutkan kata sesuai abjad
my_str  = input("Enter a string: ")
my_str = input("i want to be a programmer")
words = my_str.split()
words.sort()
for word in words:
    print(word)




