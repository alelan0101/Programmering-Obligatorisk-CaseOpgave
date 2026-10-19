import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
print("")
print("Udskrift af students databasen\n------------------------------------------------------------------------------------------------------------------------")
print("id, uddannelse_id, navn, addresse, email, fødselsdag, telefon_nummer\n------------------------------------------------------------------------------------------------------------------------")
for row in cursor.fetchall():
    print(row)

print("")
print("Udskrift af uddannelse databasen\n------------------------------------------------------------------------------------------------------------------------")
print("id, navn\n------------------------------------------------------------------------------------------------------------------------")
cursor.execute("SELECT * FROM uddannelse")
for row in cursor.fetchall():
    print(row)
