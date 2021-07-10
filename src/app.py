from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MySQL_DATABASE_HOST'] = 'localhost'
app.config['MySQL_DATABASE_USER'] = 'root'
app.config['MySQL_DATABASE_PASSWORD'] = 'tano1234' 
app.config['MySQL_DATABASE_DB'] = 'empleados'

mysql.init_app(app)


if __name__ == '__main__':
    app.run(debu=True)