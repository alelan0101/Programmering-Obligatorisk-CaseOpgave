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
    else:
        print("Sletter person", find, "fra Studernde")
        cursor.execute("DELETE FROM students WHERE id=?", (find,))
elif intput == "uddannelse":
    find=str(input("Hvilken person ønsker du at slette?"))
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    if find == "alt":
        print("Sletter alt fra uddannelse")
        cursor.execute("DELETE FROM uddannelse")
    else:
        print("Sletter person", find, "fra uddannelse")
        cursor.execute("DELETE FROM uddannelse WHERE id=?", (find,))
else:
    print("Ugyldig input")