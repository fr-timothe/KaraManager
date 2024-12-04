from flask import Flask, render_template, request, url_for, flash, redirect
from database_manager import DatabaseManager

app = Flask(__name__)
db_manager = DatabaseManager()
en_salle=10
total_argent=3350

@app.route('/')
def index():
    return render_template('index.html', en_salle=en_salle, total_argent=total_argent)

@app.route('/rooms')
def rooms():
    return render_template('rooms/list.html', attributes=db_manager.get_attrubutes("rooms"), rooms=db_manager.get_rooms())

@app.route('/rooms/<int:id>')
def room(id):
    if db_manager.record_exists("rooms", id):
         return render_template('rooms/info.html', room_info=db_manager.get_room(id))
    else:
        return redirect(url_for('rooms'))
    
@app.route('/rooms/create', methods=('GET', 'POST'))
def create_room():
    if request.method == 'POST':
        db_manager.add_room(request.form['nom_salle'], request.form['nbr_places'], request.form['prix_heure'])
        return redirect(url_for('rooms'))
    else:
        return render_template('rooms/create.html')

@app.route('/rooms/<int:id>/delete', methods=('GET', 'POST'))
def delete_room(id):
    if request.method == 'POST':
        if db_manager.record_exists("rooms", id):
            db_manager.del_room(id)
            return redirect(url_for('rooms'))
        else:
            return redirect(url_for('rooms'))
    else:
        return render_template('rooms/delete.html', room_id=id)

@app.route('/clients')
def clients():
    return render_template('clients/list.html', attributes=db_manager.get_attrubutes("clients"), clients=db_manager.get_clients())

@app.route('/clients/<int:id>')
def client(id):
    if db_manager.record_exists("clients", id):
         return render_template('clients/info.html', client_info=db_manager.get_client(id))
    else:
        return redirect(url_for('clients'))

@app.route('/clients/create', methods=('GET', 'POST'))
def create_client():
    if request.method == 'POST':
        db_manager.add_client(request.form['nom'], request.form['prenom'], request.form['email'], request.form['telephone'])
        return redirect(url_for('clients'))
    else:
        return render_template('clients/create.html')

@app.route('/clients/<int:id>/delete', methods=('GET', 'POST'))
def delete_client(id):
    if request.method == 'POST':
        if db_manager.record_exists("clients", id):
            db_manager.del_client(id)
            return redirect(url_for('clients'))
        else:
            return redirect(url_for('clients'))
    else:
        return render_template('clients/delete.html', client_id=id)

@app.route('/orders')
def orders():
    return render_template('orders/list.html', attributes=db_manager.get_attrubutes("orders"), clients=db_manager.get_orders())

@app.route('/infos')
def infos():
    return render_template('infos.html')

if __name__ == '__main__':
    app.run(debug=True)