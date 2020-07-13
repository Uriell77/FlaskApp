from flask import Blueprint

#creo un modulo(Blueprint)
register = Blueprint('register', __name__, static_folder='static', template_folder='templates')
