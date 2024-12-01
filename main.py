from flask import Flask, render_template
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

@app.route('/orders')
def orders():
    return render_template('orders.html', attributes=db_manager.get_attrubutes("orders"), clients=db_manager.get_orders())

@app.route('/infos')
def infos():
    return render_template('infos.html')

if __name__ == '__main__':
    app.run(debug=True)