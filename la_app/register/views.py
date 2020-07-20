
#importo el blueprint register 
from la_app import register
from flask import render_template, request

#primera vista de la app
@register.route('/reg', methods=['GET', 'POST'])
def register():
	return render_template('register.html')

