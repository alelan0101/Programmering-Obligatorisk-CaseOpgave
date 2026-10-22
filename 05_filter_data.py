import sqlite3
i = 0
hvor=input(str("Hvilken tabel søger du I? ")).lower()
id = input(str("Hvilket kolonne ønsker du at bruge? "))
spec = input(str("Sekundær kolonne: "))
#Skriv hvad du leder efter så printer den det hele
conn = sqlite3.connect('students.db')
cursor=conn.cursor()
SearchSTR = str(id)
SearchSTR2 = str(spec)
CursorCommand = (F"SELECT {SearchSTR}, {SearchSTR2}  from  {hvor}")
#print(P1)
obj = cursor.execute(CursorCommand)
for row in obj:
    print(row)