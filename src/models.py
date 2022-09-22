from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)

    def __repr__(self):  #OJO CON DOBLE LINEA
        return '<User %r>' % self.id  #LA INSTAZACION --> ESTAS PIDIENDO UNA LA CLASE QUE ESTAS CREANDO SE CONVIERTA EN UN OBJ
        #CASTEAR = TRADUCIR EL RESULTADO
        
    def serialize(self): #MUCHO OJO LA FUNCIÓN serialize TRANSFORMÁS LA ETIQUETA ILEGIBLE CON QUE TE RESPONDE PYTHON EN UN OBJETO LEGIBLE
        return {        #FORMULA PARA CREAR ESE PASO (instazacion)
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

            # do not serialize the password, its a security breach

#OJO: AQUÍ HACEMOS LA TABLA DE DE Planets
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    favorites = db.relationship('Favorites', backref='planets', lazy=True)


    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'),
       nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'),
       nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id,
            # do not serialize the password, its a security breach
        }


        #OJO: AQUÍ HACEMOS LA TABLA DE DE People
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    favorites = db.relationship('Favorites', backref='people', lazy=True)


    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            # do not serialize the password, its a security breach
        }