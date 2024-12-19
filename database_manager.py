import sqlite3
import date_manager

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
            telephone TEXT NOT NULL
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
    
    def get_attrubutes(self, table:str):
        # Récupère les informations des colonnes d'une table
        return self.curseur.execute("PRAGMA table_info(?)"(table)).fetchall()

    def arbitrary_query(self, query):
        # Exécute une requête SQL arbitraire
        self.curseur.execute(query)
        self.connexion.commit()

    def get_rooms(self):
        # Récupère toutes les salles
        return self.curseur.execute("SELECT * FROM rooms").fetchall()
    
    def get_room(self, id:int):
        # Récupère une salle par son ID
        return self.curseur.execute("SELECT * FROM rooms WHERE id=?"(id)).fetchone()
    
    def add_room(self, nom_salle:str, nbr_places:int, prix_heure:float):
        # Ajoute une nouvelle salle
        self.curseur.execute("INSERT INTO rooms (nom_salle, nbr_places, prix_heure) VALUES (?, ?, ?)", (nom_salle, nbr_places, prix_heure))
        self.connexion.commit()

    def del_room(self, id:int):
        # Supprime une salle par son ID
       self.curseur.execute("DELETE FROM rooms WHERE id=?"(id))
       self.connexion.commit()
    
    def update_room(self, id:int, nom_salle:str, nbr_places:int, prix_heure:float):
        self.curseur.execute("UPDATE rooms SET nom_salle=?, nbr_places=?, prix_heure=? WHERE id=?", (nom_salle, nbr_places, prix_heure, id))
        self.connexion.commit()

    def get_clients(self):
        # Récupère tous les clients
        return self.curseur.execute("SELECT * FROM clients").fetchall()
    
    def get_client(self, id:int):
        # Récupère un client par son ID
        return self.curseur.execute("SELECT * FROM clients WHERE id=?"(id)).fetchone()
    
    def add_client(self, nom:str, prenom:str, email:str="NULL", telephone:str="NULL"):
        # Ajoute un nouveau client
        self.curseur.execute("INSERT INTO clients (nom, prenom, email, telephone) VALUES (?, ?, ?, ?)", (nom, prenom, email, telephone))
        self.connexion.commit()

    def client_exist(self, nom:str, prenom:str):
        self.curseur.execute("SELECT * FROM clients WHERE nom=? AND prenom=?", (nom, prenom))
        return self.curseur.fetchone()
    
    def del_client(self, id:int):
        # Supprime un client par son ID
       self.curseur.execute("DELETE FROM clients WHERE id=?"(id))
       self.connexion.commit()
    
    def update_client(self, id:int, nom:str, prenom:str, email:str="NULL", telephone:str="NULL"):
        self.curseur.execute("UPDATE clients SET nom=?, prenom=?, email=?, telephone=? WHERE id=?", (nom, prenom, email, telephone, id))
        self.connexion.commit()

    def add_order(self, id_client:int, id_salle:int, nbr_heure:int, date_reservation:str):
        # Ajoute une nouvelle commande
        self.curseur.execute("INSERT INTO orders (id_client, id_salle, nbr_heure, date_reservation) VALUES (?, ?, ?, ?)", (id_client, id_salle, nbr_heure, date_reservation))
        self.connexion.commit()

    def get_orders(self):
        # Récupère toutes les commandes
        return self.curseur.execute("SELECT * FROM orders").fetchall()

    def get_order(self, id:int):
        # Récupère un client par son ID
        return self.curseur.execute("SELECT * FROM orders WHERE id=?"(id)).fetchone()
    
    def del_orders(self, id:int):
        # Supprime une commande par son ID
        self.curseur.execute("DELETE FROM orders WHERE id=?"(id))

    def update_orders(self, id:int, id_salle:int, nbr_heure:int, date_reservation:str):
        self.curseur.execute("UPDATE orders SET id_salle=?, nbr_heure=?, date_reservation=? WHERE id=?", (id_salle, nbr_heure, date_reservation, id))
        self.connexion.commit()
    
    def get_client_order(self, id:int, id_clients:int, date_reservation:int):
        # Récupère une commande spécifique
        return self.curseur.execute("SELECT date_reservation FROM orders JOIN clients ON ",(id_clients.orders=id.clients.clients)).fetchone()

    def get_next_orders(self):
        sorted_orders = []
        date_now=date_manager.date_time_now()
        order_day = self.curseur.execute("SELECT * FROM orders WHERE date_reservation LIKE ?", (date_manager.date_now() + '%',)).fetchall()
        for order in order_day:
            if date_manager.date_to_datetime(order[4]) > date_manager.date_to_datetime(date_now):
                client = self.get_client(order[1])
                client_name = f"{client[1]} {client[2]}"
                temp = [order[0], client_name, self.get_room(order[2])[1], order[3], order[4]]
                sorted_orders.append(temp)
        return sorted_orders
        

    def record_exists(self, table:str, id:int):
        # Vérifie si un enregistrement existe dans une table par son ID
        self.curseur.execute(f"SELECT 1 FROM {table} WHERE id=?", (id,))
        return self.curseur.fetchone() is not None