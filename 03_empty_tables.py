#Script for delete

import sqlite3

intput = input(str("Hvilken table ønsker du at slette fra?")).lower()
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
        cursor.execute("DELETE FROM students WHERE navn=?", (find,))
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
        cursor.execute("DELETE FROM uddannelse WHERE navn=?", (find,))
        conn.commit()
else:
    print("Ugyldig input")