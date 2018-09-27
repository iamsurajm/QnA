from flask import Flask, request, render_template

import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(host="localhost", user="root", passwd="", db="qna")
cur = db.cursor()

@app.route('/')
def home():
    return render_template('blog.html')

@app.route('/signin')
def index():
    return render_template('main.html')

@app.route('/check',methods=["GET","POST"])
def check():
    db = mysql.connector.connect(host="localhost", user="root", passwd="", db="qna")
    cur = db.cursor()
    if request.method == "POST":
        user = request.form['username']
        pas = request.form['password']
        cur.execute("SELECT COUNT(1) FROM users WHERE username=%s;",[user])
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM users WHERE username=%s;", [user])
            for row in cur.fetchall():
                if pas == row[0]:
                    print("Successfull")
                    return render_template("blog.html")
                else:
                    return render_template("signup.html")
        else:
            return render_template("signup.html")
        db.close()

@app.route('/signup',methods=['GET','POST'])
def signup():
    return render_template('signup.html')
@app.route('/create',methods=['GET','POST'])
def create():
    db = mysql.connector.connect(host="localhost", user="root", passwd="", db="qna")
    cur = db.cursor()
    if request.method =="POST":
        user = request.form["username"]
        emal = request.form["email"]
        pas = request.form["password"]
        cur.execute("insert into users (username,email,password) values (%s,%s,%s);",(user,emal,pas))
        db.commit()
        db.close()
        return render_template("main.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)