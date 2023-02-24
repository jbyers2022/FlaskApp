from app import app
from flask import render_template, flash, redirect, url_for, jsonify
from app.forms import LoginForm

@app.route('/')


@app.route('/json')
def jsonTest():
	instructor={"username":"jbyers","role":"student"}
	return jsonify(instructor)


@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Welcome user {}! Opted for remember_me={}'.format(form.username.data, form.remember_me.data))
		return render_template('jack.html')
	return render_template('login.html', title='Sign In', form=form)

@app.route('/index')
def index():
	user = {'username':'jbyers'}
	classes = [{'classInfo':{'code':'CSC324','title':'DevOps'},'instructor':'B Yan'}]
	return render_template('index.html', title='Home', user=user, classes=classes)
