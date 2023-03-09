from flask import Flask, render_template
from flask_mysqldb import MySQL
import mysql.connector
from constants import *

app = Flask(__name__)
# disables Flask's alphabetical organization of json itens
app.config['JSON_SORT_KEYS'] = False

# sets the config to connect to database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd= DBPASSWORD,
    database='API'
)
cur = mydb.cursor()

# execute the function when user gets to home page
@app.route('/')
def Home():
    # cur.execute(f"insert into Movies(idMov, name) values(11, 'teste')")
    # cur.execute(f"delete from Movies where idMov = 11")
    # mydb.commit()
    cur.execute('select * from Movies')
    result = cur.fetchall()
    movies = list()
    for movie in result:
        movies.append(
            {
            'id': movie[0],
            'name': movie[1],
            'year': movie[2],
            'duration': movie[3]
            }
        )
    return render_template('index.html', data=movies)

app.run(port=5000, host='localhost',debug=True)