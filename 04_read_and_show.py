import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
print("Udskrift af students databasen\n----------------------------------------------------------------------------------------------------------------------------------")

print(f"{'id':<5}{'uddannelse_id':<16}{'Navn':<22}{'Addresse':<32}{'Email':<32}{'Fødselsdag':<12}{'Telefon':<14}")
for row in cursor.fetchall():
    print(f"{row[0]:<5}{row[1]:<16}{row[2]:<22}{row[3]:<32}{row[4]:<32}{row[5]:<12}{row[6]:<14}")

print("----------------------------------------------------------------------------------------------------------------------------------")
print("Udskrift af uddannelse databasen\n------------------------------------------------------------------------------------------------------------------------")
cursor.execute("SELECT * FROM uddannelse")
print(f"{'id':<5}{'Navn':<15}")
for row in cursor.fetchall():
    print(f"{row[0]:<5}{row[1]:<15}")
