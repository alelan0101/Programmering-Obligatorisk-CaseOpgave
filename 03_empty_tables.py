#Script for delete

import sqlite3

intput = input(str("Hvilken table ønsker du at slette fra?")).lower()
#Bruges til at finde ud af hvor der søges. Nedenunder identificeret prgorammet hvad du forsøger at fjerne fra den liste.
if intput == "studerende":
    find = input(str("Hvilken person ønsker du at slette?"))
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    if find == "alt":
        print("Sletter alt fra students")
        cursor.execute("DELETE FROM students")
        conn.commit()
    else:
        print("Sletter person", find, "fra Studernde")
        Shoot = ("DELETE FROM students WHERE navn='")
        Shoot=Shoot.__add__(find)
        Shoot=Shoot.__add__("'")
        cursor.execute(Shoot)
        conn.commit()
elif intput == "uddannelse":
    find=str(input("Hvilken person ønsker du at slette?"))
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    if find == "alt":
        print("Sletter alt fra uddannelse")
        cursor.execute("DELETE FROM uddannelse")
        conn.commit()
    else:
        print("Sletter person", find, "fra uddannelse")
        Shoot = ("DELETE FROM uddannelse WHERE navn='")
        Shoot=Shoot.__add__(find)
        Shoot=Shoot.__add__("'")
        cursor.execute(Shoot)
        conn.commit()
else:
    print("Ugyldig input")