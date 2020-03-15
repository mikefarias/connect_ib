from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object('config')

from .views import price
from .routes import routes