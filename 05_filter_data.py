import sqlite3
i = 0
hvor=input(str("Hvilken tabel søger du I? ")).lower()
#Skriv hvad du leder efter så printer den det hele
conn = sqlite3.connect('students.db')
cursor=conn.cursor()

searchKolonne = input("Hvilken kolonne findes dette data I: ")
what = input(str("Hvad søger du efter: "))
CursorCommand = (F"SELECT *  from  {hvor} where {searchKolonne} LIKE '%{what}%'")

    
#print(P1)
obj = cursor.execute(CursorCommand)
for row in obj:
    print(row)