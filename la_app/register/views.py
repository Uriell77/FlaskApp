
#importo el blueprint register 
from la_app import register
from flask import render_template, request, flash

#primera vista de la app
@register.route('/reg', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		mens = 'Passwords no concuerdan'
		flash(mens)
		return render_template('register.html', title='Registro', sti='d-block')
	else:
		return render_template('register.html', sti='d-none', title='Registro')

