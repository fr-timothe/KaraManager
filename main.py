from flask import Flask, render_template, request, url_for, flash, redirect
from database_manager import DatabaseManager

app = Flask(__name__)
db_manager = DatabaseManager()
en_salle = 10
total_argent = 3350

@app.route('/')
def index():
    # Route pour la page d'accueil
    return render_template('index.html', en_salle=en_salle, total_argent=total_argent)

@app.route('/rooms')
def rooms():
    # Route pour afficher la liste des salles
    return render_template('rooms/list.html', attributes=db_manager.get_attrubutes("rooms"), rooms=db_manager.get_rooms())

@app.route('/rooms/<int:id>')
def room(id):
    # Route pour afficher les détails d'une salle spécifique
    if db_manager.record_exists("rooms", id):
        # Si la salle existe, afficher ses détails
        return render_template('rooms/info.html', room_info=db_manager.get_room(id))
    else:
        # Sinon, rediriger vers la liste des salles
        return redirect(url_for('rooms'))

@app.route('/rooms/create', methods=('GET', 'POST'))
def create_room():
    # Route pour créer une nouvelle salle
    if request.method == 'POST':
        # Si la méthode est POST, ajouter la salle avec les données du formulaire
        db_manager.add_room(request.form['nom_salle'], request.form['nbr_places'], request.form['prix_heure'])
        return redirect(url_for('rooms'))
    else:
        # Sinon, afficher le formulaire de création de salle
        return render_template('rooms/create.html')

@app.route('/rooms/<int:id>/delete', methods=('GET', 'POST'))
def delete_room(id):
    # Route pour supprimer une salle
    if request.method == 'POST':
        # Si la méthode est POST, vérifier si la salle existe
        if db_manager.record_exists("rooms", id):
            # Si la salle existe, la supprimer
            db_manager.del_room(id)
            return redirect(url_for('rooms'))
        else:
            # Sinon, rediriger vers la liste des salles
            return redirect(url_for('rooms'))
    else:
        # Sinon, afficher le formulaire de suppression de salle
        return render_template('rooms/delete.html', room_id=id)

@app.route('/clients')
def clients():
    # Route pour afficher la liste des clients
    return render_template('clients/list.html', attributes=db_manager.get_attrubutes("clients"), clients=db_manager.get_clients())

@app.route('/clients/<int:id>', methods=('GET', 'POST'))
def client(id):
    if request.method == 'POST':
        if db_manager.record_exists("clients", id):
            db_manager.update_client(id, request.form['nom'], request.form['prenom'], request.form['email'], request.form['telephone'])
            return redirect(url_for('clients'))
        else:
            return redirect(url_for('clients'))
    else:
        # Route pour afficher les détails d'un client spécifique
        if db_manager.record_exists("clients", id):
            # Si le client existe, afficher ses détails
            return render_template('clients/info.html', client_info=db_manager.get_client(id))
        else:
            # Sinon, rediriger vers la liste des clients
            return redirect(url_for('clients'))

@app.route('/clients/create', methods=('GET', 'POST'))
def create_client():
    # Route pour créer un nouveau client
    if request.method == 'POST':
        # Si la méthode est POST, ajouter le client avec les données du formulaire
        db_manager.add_client(request.form['nom'], request.form['prenom'], request.form['email'], request.form['telephone'])
        return redirect(url_for('clients'))
    else:
        # Sinon, afficher le formulaire de création de client
        return render_template('clients/create.html')

@app.route('/clients/<int:id>/delete', methods=('GET', 'POST'))
def delete_client(id):
    # Route pour supprimer un client
    if request.method == 'POST':
        # Si la méthode est POST, vérifier si le client existe
        if db_manager.record_exists("clients", id):
            # Si le client existe, le supprimer
            db_manager.del_client(id)
            return redirect(url_for('clients'))
        else:
            # Sinon, rediriger vers la liste des clients
            return redirect(url_for('clients'))
    else:
        # Sinon, afficher le formulaire de suppression de client
        return render_template('clients/delete.html', client_id=id)

@app.route('/orders')
def orders():
    # Route pour afficher la liste des commandes
    return render_template('orders/list.html', attributes=db_manager.get_attrubutes("orders"), clients=db_manager.get_orders())

@app.route('/infos')
def infos():
    # Route pour afficher des informations générales
    return render_template('infos.html')

#if __name__ == '__main__':
    # Démarrage de l'application Flask en mode debug
    #app.run(debug=True)