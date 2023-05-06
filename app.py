from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:j73987927j@localhost/tienda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/utecshop/*": {"origins": "*"}})

from models import Usuario,Producto,Compra
with app.app_context():
    db.create_all()

from routes import login_bp
app.register_blueprint(login_bp, url_prefix="/")
