
# import sqlite3
import sqlite3

# lave connection med databasen students
conn = sqlite3.connect("students.db")

#initialisere variabel cursor
cursor = conn.cursor()

#opretter en tabel med databasen
cursor.execute("""
CREATE TABLE if not exists students (
    id INTEGER PRIMARY KEY,
    uddannelse_id INTEGER,
    navn TEXT,
    addresse TEXT,
    e-mail TEXT,
    fødselsdag TEXT,
    telefon_nummer TEXT,
    
    FOREIGN KEY (uddannelse_id) REFERENCES uddannelse(id) 
)

""")

# table uddannelse
cursor.execute("""
CREATE TABLE if not exists uddannelse (
    id INTEGER PRIMARY KEY,
    navn TEXT
    
)
""")
conn.close()