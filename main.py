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
    return render_template('rooms.html')

@app.route('/clients')
def clients():
    return render_template('clients.html', attributes=db_manager.get_attrubutes("clients"), clients=db_manager.get_clients())

@app.route('/clients/<int:id>')
def client(id):
    if db_manager.record_exists("clients", id):
        return render_template('info_client.html', client_info=db_manager.get_client(id))
    else:
        return redirect(url_for('clients'))
    
@app.route('/clients/<int:id>/delete', methods=('GET', 'POST'))
def delete_client(id):
    if request.method == 'POST':
        db_manager.del_clients(id)
        return redirect(url_for('clients'))
    else:
        return render_template('delete_client.html', client_id=id)

@app.route('/clients/create', methods=('GET', 'POST'))
def create_client():
    if request.method == 'POST':
        db_manager.add_client(request.form['nom'], request.form['prenom'], request.form['email'], request.form['telephone'])
        return redirect(url_for('clients'))
    else:
        return render_template('create_client.html')

@app.route('/orders')
def orders():
    return render_template('orders.html', attributes=db_manager.get_attrubutes("orders"), clients=db_manager.get_orders())

@app.route('/infos')
def infos():
    return render_template('infos.html')

if __name__ == '__main__':
    app.run(debug=True)