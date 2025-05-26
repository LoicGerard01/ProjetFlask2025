from datetime import date
from flask import render_template, session

from . import app, models

@app.route('/')
def accueil():
    today = date.today()
    representations = (
        models.Representation.query
        .filter(models.Representation.date_representation > today)
        .order_by(models.Representation.date_representation.asc())
        .limit(3)
        .all()
    )
    return render_template('accueil.html', title="Accueil", representations=representations)

@app.route('/programmes')
def programmes():
    today = date.today()
    liste_representations = models.Representation.query.filter(models.Representation.date_representation>today).order_by(models.Representation.date_representation.asc()).all()
    return render_template('programmes.html', title="Nos programmes", representations=liste_representations)


@app.route('/clients')
def clients():
    liste_clients = models.Client.query.all()
    return render_template('clients.html', title="Clients", liste_clients=liste_clients)

@app.route('/representations')
def representations():
    liste_representations = models.Representation.query.all()
    return render_template('representations.html', title="Représentations", liste_representations=liste_representations)

@app.route('/representation/<int:id>')
def detail_representation(id):
    rep = models.Representation.query.get_or_404(id)
    return render_template('representation_detail.html', title=rep.titre, representation=rep)


@app.route('/reservations')
def reservations():
    liste_reservations = models.Reservation.query.all()
    return render_template('reservations.html', title="Réservations", liste_reservations=liste_reservations)

@app.route('/salles')
def salles():
    liste_salles = models.Salle.query.all()
    return render_template('salles.html', title="Salles", liste_salles=liste_salles)

