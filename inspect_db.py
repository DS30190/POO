import sqlite3

# Nom du fichier de base de données SQLite
db_file = 'db.sqlite3'

# Connectez-vous à la base de données SQLite
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

try:
    # Affichez les tables dans la base de données
    print("Tables dans la base de données:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])

    # Affichez le schéma de la table 'consultation_media'
    print("\nSchéma de la table 'consultation_media':")
    cursor.execute("PRAGMA table_info(consultation_media);")
    columns = cursor.fetchall()
    for column in columns:
        print(column)

except sqlite3.OperationalError as e:
    print(f"Erreur d'opération : {e}")

finally:
    # Fermez la connexion à la base de données
    conn.close()
