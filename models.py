from . import db


class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.String(50), nullable=False)
    prenom_client = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    mobile = db.Column(db.String(50), nullable=True, unique=True)

    def __repr__(self):
        return f"{self.nom_client} {self.prenom_client} ({self.email}) - {self.mobile} - {self.id_client} - {self.reservations} "


class Representation(db.Model):
    id_representation = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    date_representation = db.Column(db.Date, nullable=True)
    image = db.Column(db.String(50), nullable=True , default='image.jpg')

    def __repr__(self):
        return f"{self.titre} ({self.type}) - {self.date_representation} - {self.id_representation} - {self.reservations} - {self.image} "


class Reservation(db.Model):
    id_reservation = db.Column(db.Integer, primary_key=True)
    date_reservation = db.Column(db.TIMESTAMP, nullable=False)
    id_client = db.Column(db.Integer, db.ForeignKey('client.id_client'), nullable=False)
    id_representation = db.Column(db.Integer, db.ForeignKey('representation.id_representation'), nullable=False)
    id_salle = db.Column(db.Integer, db.ForeignKey('salle.id_salle'), nullable=False)

    def __repr__(self):
        return f"{self.date_reservation} - {self.id_client} - {self.id_representation} - {self.id_salle} - {self.id_reservation} "


class Salle(db.Model):
    id_salle = db.Column(db.Integer, primary_key=True)
    num_salle = db.Column(db.String(50), nullable=False, unique=True)
    nb_sieges = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.num_salle} - {self.nb_sieges} - {self.id_salle} - {self.reservations} "