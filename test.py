from flask import Flask, request, render_template
import MySQLdb
app = Flask(__name__)
conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="qna")
cur = conn.cursor()


@app.route('/',methods=["GET","POST"])
def main():
    return render_template('login.html')

@app.route('/check',methods=["GET","POST"])
def check():
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


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/hhg')
def blog():
    return render_template('blog.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def newDatabase():
    query = "insert into users (username,email,password) values (%s,%s,%s)"
    if request.method == 'POST':
        nm = str(request.form['nm'])
        email = str(request.form['email'])
        pwd = str(request.form['pwd'])
        cur.execute(query, (nm, email, pwd))
        conn.commit()
        conn.close()
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
