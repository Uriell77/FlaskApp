from flask import Flask #importo flask
from .register import register # importo el blueprint register
from . register  import views # importo el archivo views porque lo trae el blueprint register sino no se va ver
import os 
from flask import send_from_directory, render_template  
from .login import login, views

#creo la instancia app de flask
app = Flask(__name__)

#registro el blueprint "register" en la app (objeto flask)
app.register_blueprint(register)
app.register_blueprint(login)

# para evitar el 404 de favicon
@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def entrada():
	return render_template('entrada.html')