from flask import render_template
from . import app, models

@app.route('/')
def accueil():
    return render_template('accueil.html', title="Accueil")

@app.route('/clients')
def clients():
    liste_clients = models.Client.query.all()
    return render_template('clients.html', title="Clients", liste_clients=liste_clients)

@app.route('/representations')
def representations():
    liste_representations = models.Representation.query.all()
    return render_template('representations.html', title="Représentations", liste_representations=liste_representations)

@app.route('/reservations')
def reservations():
    liste_reservations = models.Reservation.query.all()
    return render_template('reservations.html', title="Réservations", liste_reservations=liste_reservations)

@app.route('/salles')
def salles():
    liste_salles = models.Salle.query.all()
    return render_template('salles.html', title="Salles", liste_salles=liste_salles)
