from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

  

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    hair_color = db.Column(db.String(100), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    weight = db.Column(db.Integer, unique=False, nullable=False)
    eye_color = db.Column(db.String(100), unique=False, nullable=False)
    skin_color = db.Column(db.String(100), unique=False, nullable=False)
    gender = db.Column(db.String(100), unique=False, nullable=False)
    film = db.Column(db.String(250), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "height": self.height,
            "weight": self.weight,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "gender": self.gender,
            "film": self.film,

        }  

class Starships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=False)
    type_of = db.Column(db.String(100), unique=False, nullable=False)
    speed = db.Column(db.Integer, unique=False, nullable=False)
    capacity = db.Column(db.String(100), unique=False, nullable=False)
    weight = db.Column(db.Integer, unique=False, nullable=False)
    film = db.Column(db.String(250), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "type_of": self.type_of,
            "speed": self.speed,
            "capacity": self.capacity,
            "weight": self.weight,
            "film": self.film,

        }   

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    temperature = db.Column(db.String(80), unique=False, nullable=False)
    weather = db.Column(db.String(150), unique=False, nullable=False)
    size = db.Column(db.Integer, unique=False, nullable=False)
    vegetation = db.Column(db.String(100), unique=False, nullable=False)
    natives = db.Column(db.db.String(150), unique=False, nullable=False)
    wild_life = db.Column(db.db.String(150), unique=False, nullable=False)
    natural_resources = db.Column(db.db.String(150), unique=False, nullable=False)
    film = db.Column(db.String(250), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "temperature": self.temperature,
            "weather": self.weather,
            "size": self.size,
            "vegetation": self.vegetation,
            "natives": self.natives,
            "wild_life": self.wild_life,
            "natural_resources": self.natural_resources,
            "film": self.film,

        }                 