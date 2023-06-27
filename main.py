from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3


app = Flask(__name__)
 
 
app.secret_key = 'your secret key'


@app.route('/', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        query = "SELECT * FROM users WHERE username=? AND password=?"
        result = c.execute(query, (username, password)).fetchone()

        conn.close()

        if result:
            # The username and password are correct
            session['username'] = username
            return redirect('/Home')
        else:
            # The username and password are incorrect
            return "Incorrect username or password. Try again."

    return render_template("login.html")

@app.route('/Home')
def home():
    if 'username' in session:
        return render_template('index.html')
    return redirect('/login')
@app.route('/men')
def men():
    return render_template('men.html')

@app.route('/cart')
def cart():
    if 'men' not in session:
        session['cart']=[]
    if request.method == 'POST':
        product_id=request.form(product_id)
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(f"SELECT name,price,images FROM products WHERE id='product_id'")
        product=c.fetchone()
        conn.close()
        session['cart'].append({'id' : product[0] , 'name' : product[1] , 'price' : product[2] , 'image' : product[4]})
    cart_items=session['cart']
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
        




