import sqlite3

database_fil = "students.db"

# Sørg for, at fremmednøgler faktisk bliver kontrolleret af SQLite
connection = sqlite3.connect(database_fil)
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

# Hvis tabellerne allerede har data, skal vi ikke indsætte det samme igen
cursor.execute("SELECT COUNT(*) FROM students")
antal_students = cursor.fetchone()[0]
if antal_students > 0:
    print(f"Tabellen students indeholder allerede {antal_students} rækker - "
          f"kør 03_empty_tables.py først, hvis du vil indsætte data igen.")
    connection.close()
    raise SystemExit

# ---------------------------------------------------------------
# Tabel 1: Uddanelse
# ---------------------------------------------------------------
uddannelser = [
    ("Datamatiker",),
    ("Bygningskonstruktør",),
    ("Automatiktekniker",),
    ("EUX Byg",),
    ("Handelsuddannelse (HG)",),
]

for uddannelse in uddannelser:
    cursor.execute("INSERT INTO uddannelse (navn) VALUES (?)", uddannelse)

# ---------------------------------------------------------------
# Tabel 2: students (100 rækker)
# Hver linje er: (navn, addresse, email, fødselsdag, uddannelse_id, telefon_nummer)
# ---------------------------------------------------------------
students = [
    ("Mads Andersen",      "Vesterhavsgade 12, 6700 Esbjerg",   "mads.andersen@elev.esbjerg.dk",   "2001-03-14", 1, "75 12 34 56"),
    ("Ida Kristiansen",    "Skolegade 5, 6700 Esbjerg",         "ida.kristiansen@elev.esbjerg.dk", "2000-11-02", 1, "25 44 18 90"),
    ("Lucas Sørensen",     "Kongebakken 22, 6700 Esbjerg",      "lucas.sorensen@elev.esbjerg.dk",  "2002-07-30", 2, "51 09 77 32"),
    ("Freja Hansen",       "Torvegade 3, 6700 Esbjerg",         "freja.hansen@elev.esbjerg.dk",    "2001-01-19", 2, "60 22 41 05"),
    ("Emil Nørgaard",      "Esbjergvej 88, 6710 Esbjerg V",     "emil.norgaard@elev.esbjerg.dk",   "1999-05-21", 1, "40 33 27 61"),
    ("Alma Pedersen",      "Laurbjergvej 17, 6700 Esbjerg",     "alma.pedersen@elev.esbjerg.dk",   "2003-02-08", 3, "93 65 14 27"),
    ("Noah Jensen",        "Strandbygade 40, 6700 Esbjerg",     "noah.jensen@elev.esbjerg.dk",     "2002-09-12", 1, "28 77 50 63"),
    ("Sofia Clausen",      "Hesthavej 9, 6705 Esbjerg Ø",       "sofia.clausen@elev.esbjerg.dk",   "2000-12-25", 4, "71 88 29 14"),
    ("Oliver Møller",      "Tranebærvej 33, 6700 Esbjerg",      "oliver.moller@elev.esbjerg.dk",   "2001-06-03", 2, "19 40 66 82"),
    ("Clara Bach",         "Nørrebrogade 2, 6700 Esbjerg",      "clara.bach@elev.esbjerg.dk",      "2003-04-17", 1, "30 55 91 48"),
    ("Viktor Holm",        "Ribevej 51, 6630 Rødding",          "viktor.holm@elev.esbjerg.dk",     "2000-08-27", 3, "82 13 74 59"),
    ("Maja Lindberg",      "Solbakken 7, 6700 Esbjerg",         "maja.lindberg@elev.esbjerg.dk",   "2001-10-09", 5, "61 92 35 07"),
    ("Jonas Berg",         "Guldregnvej 19, 6710 Esbjerg V",    "jonas.berg@elev.esbjerg.dk",      "2002-01-31", 2, "49 27 68 30"),
    ("Liva Winther",       "Mosevej 26, 6752 Glejbjerg",        "liva.winther@elev.esbjerg.dk",    "2003-05-22", 1, "26 71 43 85"),
    ("Sebastian Dahl",     "Havnegade 14, 6700 Esbjerg",        "sebastian.dahl@elev.esbjerg.dk",  "1999-12-08", 1, "53 84 20 76"),
    ("Astrid Krogh",       "Egevej 11, 6700 Esbjerg",           "astrid.krogh@elev.esbjerg.dk",    "2000-03-29", 4, "70 18 62 94"),
    ("Magnus Brandt",      "Kirkevej 44, 6700 Esbjerg",         "magnus.brandt@elev.esbjerg.dk",   "2001-08-16", 2, "31 96 57 20"),
    ("Ellie Simonsen",     "Birkealle 6, 6705 Esbjerg Ø",       "ellie.simonsen@elev.esbjerg.dk",  "2003-06-11", 5, "91 24 78 36"),
    ("Theodor Lund",       "Parkvej 29, 6700 Esbjerg",          "theodor.lund@elev.esbjerg.dk",    "2002-02-23", 1, "27 63 10 49"),
    ("Roberta Skaarup",    "Møllevej 13, 6700 Esbjerg",         "roberta.skaarup@elev.esbjerg.dk", "2000-07-05", 3, "58 31 86 72"),
    ("Felix Thomsen",      "Skovvejen 37, 6715 Esbjerg N",      "felix.thomsen@elev.esbjerg.dk",   "2001-11-28", 1, "64 47 92 15"),
    ("Luna Hermansen",     "Lyngvej 21, 6700 Esbjerg",          "luna.hermansen@elev.esbjerg.dk",  "2003-01-14", 4, "38 09 53 61"),
    ("Alexander Vang",     "Kystvejen 58, 6700 Esbjerg",        "alexander.vang@elev.esbjerg.dk",  "2002-04-09", 2, "72 85 26 03"),
    ("Alice Bruun",        "Rosenvej 4, 6700 Esbjerg",          "alice.bruun@elev.esbjerg.dk",     "2000-10-20", 1, "45 50 17 89"),
    ("William Salling",    "Galejvej 32, 6700 Esbjerg",         "william.salling@elev.esbjerg.dk", "2001-05-26", 5, "86 66 41 22"),
    ("Vega Holst",         "Anbækvej 16, 6700 Esbjerg",         "vega.holst@elev.esbjerg.dk",      "2003-03-07", 2, "29 72 84 53"),
    ("Anton Frost",        "Bygmarken 25, 6715 Esbjerg N",      "anton.frost@elev.esbjerg.dk",     "1999-09-18", 3, "57 14 90 68"),
    ("Nova Damgaard",      "Liljevej 8, 6700 Esbjerg",          "nova.damgaard@elev.esbjerg.dk",   "2000-06-11", 1, "33 59 21 47"),
    ("Oscar Frank",        "Grønnegade 47, 6700 Esbjerg",       "oscar.frank@elev.esbjerg.dk",     "2002-12-30", 2, "76 90 35 11"),
    ("Livia Beck",         "Vandværksvej 10, 6700 Esbjerg",     "livia.beck@elev.esbjerg.dk",      "2001-02-15", 4, "18 41 75 92"),
    ("Arthur Schmidt",     "Fabriksgade 6, 6700 Esbjerg",       "arthur.schmidt@elev.esbjerg.dk",  "2003-08-01", 1, "81 27 63 34"),
    ("Merle Jessen",       "Klintevejen 18, 6752 Glejbjerg",    "merle.jessen@elev.esbjerg.dk",    "2000-04-24", 5, "24 68 10 85"),
    ("Konrad Vester",      "Søndergade 21, 6700 Esbjerg",       "konrad.vester@elev.esbjerg.dk",   "2001-07-08", 2, "67 32 58 19"),
    ("Freja Bjerre",       "Agervej 12, 6700 Esbjerg",          "freja.bjerre@elev.esbjerg.dk",    "2002-10-13", 1, "52 77 94 40"),
    ("Storm Lindgreen",    "Anlægsgade 9, 6700 Esbjerg",        "storm.lindgreen@elev.esbjerg.dk", "1999-11-05", 3, "43 86 20 71"),
    ("Dagny Laustsen",     "Elmevej 31, 6705 Esbjerg Ø",        "dagny.laustsen@elev.esbjerg.dk",  "2000-01-27", 4, "95 48 62 26"),
    ("Malthe Ring",        "Strandvejen 65, 6700 Esbjerg",      "malthe.ring@elev.esbjerg.dk",     "2002-06-19", 1, "36 15 89 03"),
    ("Selma Præstholm",    "Fyrretræsvej 7, 6715 Esbjerg N",    "selma.praestholm@elev.esbjerg.dk","2003-09-23", 5, "78 51 36 94"),
    ("Alfred Kjær",        "Postvejen 15, 6630 Rødding",        "alfred.kjaer@elev.esbjerg.dk",    "2000-05-09", 2, "19 93 47 58"),
    ("Oda Skovgaard",      "Bakkevejen 23, 6700 Esbjerg",       "oda.skovgaard@elev.esbjerg.dk",   "2001-12-17", 1, "61 30 74 82"),
    ("Elliot Rex",         "Avenue 42, 6700 Esbjerg",           "elliot.rex@elev.esbjerg.dk",      "2002-03-03", 3, "54 26 68 90"),
    ("Ronia Carlsen",      "Munkvejen 5, 6752 Glejbjerg",       "ronia.carlsen@elev.esbjerg.dk",   "2003-07-27", 4, "87 42 19 65"),
    ("Emiliano Holmen",    "Håndværkervej 28, 6700 Esbjerg",    "emiliano.holmen@elev.esbjerg.dk", "1999-10-14", 1, "42 67 80 13"),
    ("Signe Vind",         "Vindruevejen 11, 6700 Esbjerg",     "signe.vind@elev.esbjerg.dk",      "2000-08-31", 2, "75 81 34 27"),
    ("Louka Meincke",      "Bahnevej 19, 6700 Esbjerg",         "louka.meincke@elev.esbjerg.dk",   "2001-04-06", 5, "29 53 96 41"),
    ("Johanne Sejr",       "Sejrgade 2, 6700 Esbjerg",          "johanne.sejr@elev.esbjerg.dk",    "2002-11-21", 1, "63 05 48 76"),
    ("Villum Kragh",       "Dragsholmvej 34, 6700 Esbjerg",     "villum.kragh@elev.esbjerg.dk",    "2003-02-09", 2, "58 90 12 37"),
    ("Marie Toft",         "Toftlundvej 46, 6630 Rødding",      "marie.toft@elev.esbjerg.dk",      "2000-02-27", 3, "31 74 65 08"),
    ("Nicklas Egholm",     "Egholmvej 3, 6700 Esbjerg",         "nicklas.egholm@elev.esbjerg.dk",  "2001-09-13", 1, "80 46 27 51"),
    ("Aya Jacobsen",       "Japanvej 8, 6700 Esbjerg",          "aya.jacobsen@elev.esbjerg.dk",    "2002-05-25", 4, "26 91 70 44"),
    ("Albert Vindfeldt",   "Vesterled 27, 6700 Esbjerg",        "albert.vindfeldt@elev.esbjerg.dk","2003-01-16", 5, "47 62 33 19"),
    ("Edith Marquardsen",  "Marquardsvej 14, 6700 Esbjerg",     "edith.marquardsen@elev.esbjerg.dk","2000-12-01", 1, "72 38 95 60"),
    ("Bo Rasmussen",       "Ravnvejen 36, 6715 Esbjerg N",      "bo.rasmussen@elev.esbjerg.dk",    "2001-06-20", 2, "15 83 51 74"),
    ("Elise Kaas",         "Kastrupvej 22, 6700 Esbjerg",       "elise.kaas@elev.esbjerg.dk",      "2002-08-04", 1, "64 17 29 83"),
    ("Adnan Yilmaz",       "Sportsvejen 18, 6700 Esbjerg",      "adnan.yilmaz@elev.esbjerg.dk",    "2003-04-28", 3, "39 25 61 47"),
    ("Vera Winslow",       "Winslowvej 6, 6700 Esbjerg",        "vera.winslow@elev.esbjerg.dk",    "2000-03-16", 4, "91 70 42 25"),
    ("August Storgaard",   "Storgade 50, 6700 Esbjerg",         "august.storgaard@elev.esbjerg.dk","2001-10-07", 2, "57 44 86 02"),
    ("Rosa Lindqvist",     "Lindevejen 24, 6700 Esbjerg",       "rosa.lindqvist@elev.esbjerg.dk",  "2002-01-12", 5, "68 09 73 38"),
    ("Elias Holmgård",     "Højvejen 40, 6752 Glejbjerg",       "elias.holmgaard@elev.esbjerg.dk", "1999-07-19", 1, "43 87 20 56"),
    ("Naja Winthere",      "Vintervejen 9, 6700 Esbjerg",       "naja.winthere@elev.esbjerg.dk",   "2000-11-30", 4, "75 21 94 60"),
    ("Oskar Helsted",      "Helstedsvej 13, 6700 Esbjerg",      "oskar.helsted@elev.esbjerg.dk",   "2001-05-03", 1, "30 65 48 91"),
    ("Maya Søby",          "Søbyvej 21, 6700 Esbjerg",          "maya.soby@elev.esbjerg.dk",       "2003-03-26", 2, "82 36 57 14"),
    ("Ludvig Fenger",      "Fengersvej 17, 6715 Esbjerg N",     "ludvig.fenger@elev.esbjerg.dk",   "2002-09-09", 3, "56 48 12 73"),
    ("Bettina Holm",       "Holmevejen 4, 6700 Esbjerg",        "bettina.holm@elev.esbjerg.dk",    "2000-06-22", 1, "19 74 60 28"),
    ("Aksel Brandstrup",   "Brandvejen 29, 6700 Esbjerg",       "aksel.brandstrup@elev.esbjerg.dk","2001-02-18", 5, "61 90 33 45"),
    ("Sigrid Ubbesen",     "Ubberupvej 7, 6752 Glejbjerg",      "sigrid.ubbesen@elev.esbjerg.dk",  "2003-05-31", 4, "26 53 87 09"),
    ("Pelle Kongsted",     "Kongevejen 33, 6700 Esbjerg",       "pelle.kongsted@elev.esbjerg.dk",  "2002-07-16", 2, "73 14 96 50"),
    ("Eden Lauritsen",     "Lauritsvej 11, 6700 Esbjerg",       "eden.lauritsen@elev.esbjerg.dk",  "2000-09-24", 1, "47 68 20 83"),
    ("Louise Graugaard",   "Graugaardsvej 25, 6700 Esbjerg",    "louise.graugaard@elev.esbjerg.dk","2001-12-06", 3, "38 41 75 62"),
    ("Thor Overgaard",     "Overgade 16, 6700 Esbjerg",         "thor.overgaard@elev.esbjerg.dk",  "2002-04-01", 1, "85 27 63 49"),
    ("Juna Mikkelsen",     "Møllegade 20, 6705 Esbjerg Ø",      "juna.mikkelsen@elev.esbjerg.dk",  "2003-08-13", 4, "52 93 17 06"),
    ("Anders Findsen",     "Finderupvej 39, 6630 Rødding",      "anders.findsen@elev.esbjerg.dk",  "1999-04-15", 2, "64 58 21 97"),
    ("Isabella Storm",     "Stormgade 5, 6700 Esbjerg",         "isabella.storm@elev.esbjerg.dk",  "2000-01-08", 5, "71 30 44 26"),
    ("Mikkel Fuglsang",    "Fuglsangsvej 42, 6700 Esbjerg",     "mikkel.fuglsang@elev.esbjerg.dk", "2001-08-29", 1, "15 76 68 32"),
    ("Emma Ilkjær",        "Ilkjærvej 10, 6715 Esbjerg N",      "emma.ilkjaer@elev.esbjerg.dk",    "2002-11-13", 2, "49 02 85 71"),
    ("Casper Bakken",      "Bakkegade 23, 6700 Esbjerg",        "casper.bakken@elev.esbjerg.dk",   "2003-06-05", 3, "83 55 19 04"),
    ("Tilde Wulff",        "Wulffsvej 12, 6700 Esbjerg",        "tilde.wulff@elev.esbjerg.dk",     "2000-05-28", 1, "27 41 96 58"),
    ("Ryan Chehab",        "Orientvej 8, 6700 Esbjerg",         "ryan.chehab@elev.esbjerg.dk",     "2001-03-11", 4, "57 90 62 13"),
    ("Wilma Bendtsen",     "Bendtsensvej 31, 6700 Esbjerg",     "wilma.bendtsen@elev.esbjerg.dk",  "2002-10-24", 5, "36 68 43 80"),
    ("Nohr Østergaard",    "Østergade 18, 6700 Esbjerg",        "nohr.ostergaard@elev.esbjerg.dk", "2003-02-02", 2, "74 23 58 46"),
    ("Franka Lindgreen",   "Lindgreensvej 14, 6752 Glejbjerg",  "franka.lindgreen@elev.esbjerg.dk","2000-07-14", 1, "91 46 20 73"),
    ("Ove Hvidberg",       "Hvidbergsvej 26, 6700 Esbjerg",     "ove.hvidberg@elev.esbjerg.dk",    "1999-12-21", 3, "43 81 75 29"),
    ("Smilla Nordgaard",   "Nordgardsvej 3, 6700 Esbjerg",      "smilla.nordgaard@elev.esbjerg.dk","2001-01-26", 4, "68 54 31 92"),
    ("Karl Emerek",        "Emereksvej 19, 6700 Esbjerg",       "karl.emerek@elev.esbjerg.dk",     "2002-06-13", 1, "55 09 27 64"),
    ("Stella Friis",       "Friisgade 7, 6700 Esbjerg",         "stella.friis@elev.esbjerg.dk",    "2003-04-19", 5, "22 73 80 51"),
    ("Birk Sandahl",       "Sandahlsvej 45, 6715 Esbjerg N",    "birk.sandahl@elev.esbjerg.dk",    "2000-10-03", 2, "80 62 14 37"),
    ("Ea Enevoldsen",      "Enevoldsvej 9, 6700 Esbjerg",       "ea.enevoldsen@elev.esbjerg.dk",   "2001-11-16", 1, "47 35 91 68"),
    ("Otto Justesen",      "Justesensvej 28, 6700 Esbjerg",     "otto.justesen@elev.esbjerg.dk",   "2002-03-08", 3, "59 76 42 10"),
    ("Alba Vestergaard",   "Vestergade 61, 6700 Esbjerg",       "alba.vestergaard@elev.esbjerg.dk","2003-07-27", 4, "31 88 05 74"),
    ("Rune Bechmann",      "Bechmannsvej 16, 6700 Esbjerg",     "rune.bechmann@elev.esbjerg.dk",   "2000-04-11", 2, "76 41 59 23"),
    ("Cecilie Roed",       "Roedsvej 22, 6700 Esbjerg",         "cecilie.roed@elev.esbjerg.dk",    "2001-09-06", 1, "18 53 72 96"),
    ("Tim Lyngby",         "Lyngbyvej 34, 6700 Esbjerg",        "tim.lyngby@elev.esbjerg.dk",      "2002-12-19", 5, "63 27 84 40"),
    ("Ingrid Lyberth",     "Lyberthsvej 5, 6700 Esbjerg",       "ingrid.lyberth@elev.esbjerg.dk",  "2003-01-31", 4, "92 15 67 33"),
    ("Bastián Rued",       "Ruedsvej 39, 6752 Glejbjerg",       "bastian.rued@elev.esbjerg.dk",    "1999-08-08", 2, "44 70 92 18"),
    ("Vinter Frandsen",   "Frandsensvej 24, 6700 Esbjerg",     "vinter.frandsen@elev.esbjerg.dk", "2000-02-20", 1, "27 89 36 54"),
    ("Hana Salim",         "Salimsvej 13, 6700 Esbjerg",        "hana.salim@elev.esbjerg.dk",      "2001-07-04", 3, "57 42 68 90"),
    ("Lior Gaardbo",       "Gaardbosvej 6, 6700 Esbjerg",       "lior.gaardbo@elev.esbjerg.dk",    "2002-05-17", 2, "81 30 53 26"),
    ("Yrsa Oddershede",    "Oddershedsvænge 12, 6700 Esbjerg",  "yrsa.oddershede@elev.esbjerg.dk", "2003-10-29", 1, "35 94 71 02"),
    ("Adam Poulsen",       "Poulsensvej 48, 6715 Esbjerg N",    "adam.poulsen@elev.esbjerg.dk",    "2000-06-07", 5, "69 20 84 45"),
    ("Maria Timmermann",   "Timmermannsvej 27, 6700 Esbjerg",   "maria.timmermann@elev.esbjerg.dk", "2001-04-12", 1, "50 63 27 81"),
]

# Indsæt alle students
for student in students:
    cursor.execute("""
        INSERT INTO students (navn, addresse, email, fødselsdag, uddannelse_id, telefon_nummer)
        VALUES (?, ?, ?, ?, ?, ?)
    """, student)

# Gem alle ændringerne i databasen
connection.commit()

# Vis hvor mange rækker, der nu er i tabellerne
cursor.execute("SELECT COUNT(*) FROM uddannelse")
print(f"Uddanelse indeholder nu {cursor.fetchone()[0]} rækker.")
cursor.execute("SELECT COUNT(*) FROM students")
print(f"students indeholder nu {cursor.fetchone()[0]} rækker.")

connection.close()
