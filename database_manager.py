import sqlite3

class DatabaseManager:
    def __init__(self):
        self.connexion = sqlite3.connect("lycee.sqlite3", check_same_thread=False)
        self.curseur = self.connexion.cursor()
        self.setup()

    def setup(self):
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            email TEXT,
            telephone TEXT
        )
        """)
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_salle TEXT,
            nbr_places INT,
            prix_heure FLOAT
        )
        """)
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_client INT,
            id_salle INT,
            nbr_heure INT,
            date_reservation TEXT,
            FOREIGN KEY(id_client) REFERENCES clients(id),
            FOREIGN KEY(id_salle) REFERENCES rooms(id)
        )
        """)
        self.connexion.commit()
    
    def get_attrubutes(self, table):
        return self.curseur.execute(f"PRAGMA table_info({table})").fetchall()

    def arbitrary_query(self, query):
        self.curseur.execute(query)
        self.connexion.commit()

    def add_client(self, nom, prenom, email, telephone):
        self.curseur.execute(f"INSERT INTO clients VALUES (NULL, '{nom}', '{prenom}', '{email}', '{telephone}')")
        self.connexion.commit()

    def get_clients(self):
        return self.curseur.execute("SELECT * FROM clients").fetchall()
    
    def get_client(self, id):
        self.curseur.execute(f"SELECT * FROM clients WHERE id={id}")
        return self.curseur.fetchone()
    
    def add_orders(self, id, id_salles, id_clients, nbr_heure, date_reservation ):
        self.curseur.execute(f"INSERT INTO reservation VALUES (NULL, '{id}', '{id_salles}','{id_clients}',{nbr_heure}','{date_reservation}') ")
        self.connexion.commit()

    def get_orders(self):
        self.curseur.execute("SELECT * FROM orders")
        return self.curseur.fetchall()
    
    def del_orders(self, id):
        self.curseur.execute(f"DELETE FROM orders WHERE id={id}")
        return self.curseur.fetchone()
    
    