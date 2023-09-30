from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import os

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'tests', 'templates')

app = Flask(__name__, template_folder = template_dir)


    
#Rutas de la aplicación
@app.route('/')
def home(): return render_template('index.html')

@app.route('/login_test')
def login_test(): return render_template('login_test.html')

@app.route('/register_test')
def register_test(): return render_template('register_test.html')



@app.route('/persona_edit/<string:id>', methods=["POST"])
def persona_edit(id):
    return redirect(url_for('persona'))

if __name__ == '__main__':
    app.run(port=5000)

