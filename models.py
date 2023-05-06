from app import db   

class Usuario(db.Model):
    __tablename__ = "Usuario"
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(9), nullable=False)
    adress = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    productos = db.relationship('Producto', backref='Usuario')


class Producto(db.Model):
    __tablename__ = "Producto"
    codigo_p = db.Column(db.String(6), primary_key=True)
    usuario_p = db.Column(db.String(80), db.ForeignKey('Usuario.username'))
    nombre = db.Column(db.String(40), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    marca = db.Column(db.String(30), nullable=False)
    categoria = db.Column(db.String(30), nullable=False)


class Compra(db.Model):
    __tablename__ = "Compra"
    codigo_c = db.Column(db.Integer, primary_key=True)
    codigo_p = db.Column(db.String(6), db.ForeignKey('Producto.codigo_p'))
    usuario_c = db.Column(db.String(80), db.ForeignKey('Usuario.username'))
    usuario_v = db.Column(db.String(80), db.ForeignKey('Usuario.username'))
