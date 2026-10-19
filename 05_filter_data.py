import sqlite3
i = 0
hvor=input(str("Hvilken databse søger du I? ")).lower()
id = input(str("Hvilken identifikation ønsker du at bruge? "))
spec = input(str("Sekundær identification: "))
#Skriv hvad du leder efter så printer den det hele
conn = sqlite3.connect('students.db')
cursor=conn.cursor()
SearchSTR = str(id)
SearchSTR2 = str(spec)
S1 = str("SELECT ")
S2 = S1.__add__(SearchSTR)
S3 = S2.__add__(",")
S4 = S3.__add__(SearchSTR2)
G1 = str(" from ")
G2 = G1.__add__(hvor)
P1 = S4.__add__(G2)
#print(P1)
obj = cursor.execute(P1)
for row in obj:
    print(row)