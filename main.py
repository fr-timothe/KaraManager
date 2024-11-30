from flask import Flask

main=Flask(__name__)

@app.route('/')
def welcome ():
    return "Bienvenue!"