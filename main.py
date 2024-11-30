from flask import Flask, render_template

app = Flask(__name__)
en_salle=10
total_argent=3350

@app.route('/')
def welcome ():
    return render_template('index.html', en_salle=en_salle, total_argent=total_argent)

if __name__ == '__main__':
    app.run(debug=True)