"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,redirect,request,url_for
from WbApp import app
from WbApp.tarefas import tarefa
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.',
        tarefas=tarefa.GetAll()
    )

@app.route('/detalhe/<id>')
def detalhe(id):
    """Renders the about page."""
    return render_template(
        'detalhe.html',
        title='Detalhe',
        year=datetime.now().year,
        message='Your application description page.',
        t=tarefa(1,"Enviar email")
    )

@app.route('/inserirtarefa',methods=["POST","PUT"])
def inserirtarefa():
    if request.method == "POST":
        result = request.form

        id= result["txtId"]
        desc= result["txtDesc"]
        estado= result["txtEstado"]

        t = tarefa(id,desc,estado)

        t.Inserir()
    
    return redirect(url_for('about'))


    

