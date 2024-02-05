from flask import Flask, request, render_template, redirect, url_for
import pymysql

app =  Flask(__name__)

#configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '***********'
app.config['MYSQL_PASSWORD'] = '****'
app.config['MYSQL_DB'] = 'login'

#initialize PyMySQL connection
conn = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD']
    #db=app.config['MYSQL_DB']
)

#create DATABASE and TABLE if not exists
with conn.cursor() as cursor:
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(app.config['MYSQL_DB']))
    cursor.execute("USE {}".format(app.config['MYSQL_DB']))
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR(255),
                        password VARCHAR(255)
                         )
                 """)
    conn.commit()
    
    
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods = ['POST'])
def login():
    if request.method == 'POST':
        username = request.form['u_name']
        password = request.form['u_pass']

        with conn.cursor() as cursor:
          cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)",(username, password))
          conn.commit()
        
        return redirect(url_for('index'))

        if __name__ == '__main__':
            app.run(host='0.0.0.0', port=5000, debug=True)


