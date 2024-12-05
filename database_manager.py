import sqlite3

class DatabaseManager:
    def __init__(self):
        # Connexion à la base de données SQLite
        self.connexion = sqlite3.connect("lycee.sqlite3", check_same_thread=False)
        self.curseur = self.connexion.cursor()
        self.setup()

    def setup(self):
        # Création des tables si elles n'existent pas
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT,
            telephone TEXT
        )
        """)
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_salle TEXT NOT NULL,
            nbr_places INT NOT NULL,
            prix_heure FLOAT NOT NULL
        )
        """)
        self.curseur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_client INT NOT NULL,
            id_salle INT NOT NULL,
            nbr_heure INT NOT NULL,
            date_reservation TEXT,
            FOREIGN KEY(id_client) REFERENCES clients(id),
            FOREIGN KEY(id_salle) REFERENCES rooms(id)
        )
        """)
        self.connexion.commit()
    
    def get_attrubutes(self, table):
        # Récupère les informations des colonnes d'une table
        return self.curseur.execute(f"PRAGMA table_info({table})").fetchall()

    def arbitrary_query(self, query):
        # Exécute une requête SQL arbitraire
        self.curseur.execute(query)
        self.connexion.commit()

    def get_rooms(self):
        # Récupère toutes les salles
        return self.curseur.execute("SELECT * FROM rooms").fetchall()
    
    def get_room(self, id):
        # Récupère une salle par son ID
        return self.curseur.execute(f"SELECT * FROM rooms WHERE id={id}").fetchone()
    
    def add_room(self, nom_salle, nbr_places, prix_heure):
        # Ajoute une nouvelle salle
        self.curseur.execute("INSERT INTO rooms (nom_salle, nbr_places, prix_heure) VALUES (?, ?, ?)", (nom_salle, nbr_places, prix_heure))
        self.connexion.commit()

    def del_room(self, id):
        # Supprime une salle par son ID
       self.curseur.execute(f"DELETE FROM rooms WHERE id={id}")
       self.connexion.commit()

    def get_clients(self):
        # Récupère tous les clients
        return self.curseur.execute("SELECT * FROM clients").fetchall()
    
    def get_client(self, id):
        # Récupère un client par son ID
        return self.curseur.execute(f"SELECT * FROM clients WHERE id={id}").fetchone()
    
    def add_client(self, nom, prenom, email, telephone):
        # Ajoute un nouveau client
        self.curseur.execute("INSERT INTO clients (nom, prenom, email, telephone) VALUES (?, ?, ?, ?)", (nom, prenom, email, telephone))
        self.connexion.commit()
    
    def del_client(self, id):
        # Supprime un client par son ID
       self.curseur.execute(f"DELETE FROM clients WHERE id={id}")
       self.connexion.commit()
    
    def add_orders(self, id, id_salles, id_clients, nbr_heure, date_reservation ):
        # Ajoute une nouvelle commande
        self.curseur.execute(f"INSERT INTO reservation VALUES (NULL, '{id}', '{id_salles}','{id_clients}',{nbr_heure}','{date_reservation}') ")
        self.connexion.commit()

    def get_orders(self):
        # Récupère toutes les commandes
        return self.curseur.execute("SELECT * FROM orders").fetchall()
    
    def del_orders(self, id):
        # Supprime une commande par son ID
        self.curseur.execute(f"DELETE FROM orders WHERE id={id}")
    
    def get_order(self, id, id_clients, date_reservation):
        # Récupère une commande spécifique
        return self.curseur.execute(f"SELECT {date_reservation} FROM orders JOIN clients ON {id_clients}.orders={id.clients}.clients").fetchone()
    
    def record_exists(self, table, id):
        # Vérifie si un enregistrement existe dans une table par son ID
        self.curseur.execute(f"SELECT 1 FROM {table} WHERE id=?", (id,))
        return self.curseur.fetchone() is not None