
#importo el blueprint register 
from la_app import register
from flask import render_template, request, flash, redirect, url_for
from ..register.models import *

#primera vista de la app
@register.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellido = request.form['apellido']
		correo = request.form['email']
		password = request.form['password']
		confirm = request.form['repassword']

		user = usuario(nombre, apellido, correo, password, confirm)
		if user.booleano():
			mens = "Te haz registrado correctamente"
			flash(mens)
			return render_template('login.html', sti='d-block', title='Login')
		else:
			mens = "Password no concuerdan"
			flash(mens)
			return redirect('/reg') and render_template('register.html', sti='d-block', title='Registro')

	else:
		return render_template('login.html', sti='d-none', title='Login')

