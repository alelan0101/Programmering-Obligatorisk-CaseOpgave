
import sqlite3
from datetime import datetime

database_fil = "students.db"

connection = sqlite3.connect(database_fil)
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

print("Tilføj en ny studerende")
print("-" * 40)

# Felt 1: Navn - må ikke være tom
navn = ""
while navn == "":
    navn = input("Navn: ").strip()
    if navn == "":
        print("Fejl: Navn må ikke være tomt. Prøv igen.")

# Felt 2: Addresse - må ikke være tom
addresse = ""
while addresse == "":
    addresse = input("Addresse (f.eks. 'Vestergade 1, 6700 Esbjerg'): ").strip()
    if addresse == "":
        print("Fejl: Addresse må ikke være tom. Prøv igen.")

# Felt 3: Email - skal indeholde et @ og et punktum efter @
email = ""
while email == "":
    email = input("Email: ").strip()
    # Validering af formatet
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Fejl: Email skal indeholde '@' og et domæne, f.eks. 'navn@eksempel.dk'. Prøv igen.")
        email = ""

# Felt 4: Fødselsdag - skal have formatet ÅÅÅÅ-MM-DD og
# være en rigtig dato. datetime.strptime kaster en fejl
# (ValueError), hvis datoen ikke findes, f.eks. 2001-02-30.
foedselsdag = ""
while foedselsdag == "":
    foedselsdag = input("Fødselsdag (ÅÅÅÅ-MM-DD): ").strip()
    try:
        datetime.strptime(foedselsdag, "%Y-%m-%d")  # validerer dato-format
    except ValueError:
        print("Fejl: Dato skal være gyldig og have formatet ÅÅÅÅ-MM-DD, f.eks. 2001-03-14. Prøv igen.")
        foedselsdag = ""

# Felt 5: Uddannelse - skal være et nummer fra listen.
# Vis uddannelserne fra databasen så brugeren kan vælge.
print("\nVælg en uddannelse:")
cursor.execute("SELECT id, navn FROM uddannelse ORDER BY id")
uddannelses_ider = [r[0] for r in cursor.fetchall()]
for udd_id, udd_navn in cursor.execute("SELECT id, navn FROM uddannelse ORDER BY id").fetchall():
    print(f"  {udd_id}: {udd_navn}")

uddannelse_id = ""
while uddannelse_id == "":
    tekst = input("Nummer på uddannelse: ").strip()
    if not tekst.isdigit():
        print("Fejl: Skriv et tal. Prøv igen.")
    elif int(tekst) not in uddannelses_ider:
        print("Fejl: Tallet skal være et af numrene fra listen. Prøv igen.")
    else:
        uddannelse_id = int(tekst)

# Felt 6: Telefonnummer - må kun bestå af cifre
# (mellemrum og bindestreger fjernes først)
telefon = ""
while telefon == "":
    tekst = input("Telefonnummer (f.eks. '75 12 34 56'): ").strip()
    kun_cifre = tekst.replace(" ", "").replace("-", "")
    if not kun_cifre.isdigit() or not 8 <= len(kun_cifre) <= 12:
        print("Fejl: Telefonnummer må kun bestå af cifre (8-12 stk.). Prøv igen.")
    else:
        telefon = tekst

# Indsæt den nye record med INSERT INTO
cursor.execute("""
    INSERT INTO students (navn, addresse, email, fødselsdag, uddannelse_id, telefon_nummer)
    VALUES (?, ?, ?, ?, ?, ?)
""", (navn, addresse, email, foedselsdag, uddannelse_id, telefon))
connection.commit()

# Vis den nyoprettede record så brugeren kan se, at det virkede
cursor.execute("""
    SELECT students.id, students.navn, students.addresse, students.email,
           students.fødselsdag, students.telefon_nummer, uddannelse.navn
    FROM students
    LEFT JOIN uddannelse ON students.uddannelse_id = uddannelse.id
    WHERE students.id = ?
""", (cursor.lastrowid,))
r = cursor.fetchone()
print("\nDen nye studerende er gemt:")
print(f"  id:          {r[0]}")
print(f"  Navn:        {r[1]}")
print(f"  Addresse:    {r[2]}")
print(f"  Email:       {r[3]}")
print(f"  Fødselsdag:  {r[4]}")
print(f"  Telefon:     {r[5]}")
print(f"  Uddannelse:   {r[6]}")

connection.close()
