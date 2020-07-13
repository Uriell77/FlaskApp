from flask import Blueprint

#creo un modulo(Blueprint)
login = Blueprint('login', __name__, static_folder='static', template_folder='templates')
