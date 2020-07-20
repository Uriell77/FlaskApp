
#importo el blueprint register 
from la_app import register
from flask import render_template, request, flash

#primera vista de la app
@register.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		mens = "Te haz registrado correctamente"
		return render_template('login.html', men = mens, sti='d-block')
	else:
		return render_template('login.html', sti='d-none')

