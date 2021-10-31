from flask import Flask, jsonify, request, render_template
import random
from database import *


app = Flask(  
	__name__,
	template_folder='templates',  
	static_folder='static' 
)
app.config['SECRET_KEY'] = 'changeme'


@app.route('/', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    print('going to get request')
    return render_template('signup.html')
  else:
    print('going to post request')
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    if username == "" or password == "" or email == "":
      stopbeingdumb = 'Fill all the fields'

      return render_template('signup.html')
    else:
      user = create_user(username, str(password), email)
      #DescribeUser(user)
      print(user)
      return render_template('home.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  # checking the method of request
  if request.method == 'GET':
    print('h')
    return render_template('login.html')

  # will do this if method is post
  else:
    print('something random')
    email = request.form["email"]
    password = request.form["password"]

    # checking if user filled form
    if  password == ""  or email == "":
      print("Fill all the fields")
      return render_template('login.html')
    print('hello')

    # logging user in
    user = signin(email, password)
    #DescribeUser(user)
    print(user)
    return render_template('home.html')

@app.route('/spotify')
def spotify():
  return render_template('spotify.html')

users = queryAll()
print(users)
#for user in users:
  #DescribeUser(user)

if __name__ == "__main__":
  app.run( 
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=5000,  # Randomly select the port the machine hosts on.
    debug=True
	)