#Menghitung determinan
row1 = [1,2,3]
row2 = [2,8,7]
row3 = [1,5,6]

print("\n",row1,"\n",row2,"\n",row3)

det = (row1[0]*row2[1]*row3[2]+
       row1[1]*row2[2]*row3[0]+
       row1[2]*row2[0]*row3[1]-
       row1[2]*row2[1]*row3[0]-
       row1[0]*row2[2]*row3[1]-
       row1[1]*row2[0]*row3[2])
print("determinan matriks:",det)

a11 = row2[1]*row3[2]-row2[2]*row3[1]
a12 = (-1*((row2[0]*row3[2])-(row2[2]*row3[0])))
a13 = row2[0]*row3[1]-row2[1]*row3[0]

a21 = (-1*((row1[1]*row3[2])-(row1[2]*row3[1])))
a22 = row1[0]*row3[2]-row1[2]*row3[0]
a23 = (-1*((row1[0]*row3[1])-(row1[1]*row3[0])))

a31 = row1[1]*row2[2]-row1[2]*row2[1]
a32 = (-1*((row1[0]*row2[2])-(row1[2]*row2[0])))
a33 = row1[0]*row2[1]-row1[1]*row2[0]

print("\nKofaktor matriks:")
kofaktor = [[a11, a12, a13],
            [a21, a22, a23],
            [a31, a32, a33]]
for a in range(len(kofaktor)):
    print(kofaktor[a])
