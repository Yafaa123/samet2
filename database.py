from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_user(username, password, email):
  print("Running create_user function!! ----------")
  user = User(username=username, password=password, email=email)
  existinguser = session.query(User).filter_by(email=email).first()
  print(existinguser)
  if existinguser != None:
    print('Error')
  else:
    session.add(user)
    session.commit()
    print(user)

def delete_account(username):
  session.query(User).filter_by(username = username).delete()
  session.commit()

def signin(mail, password):
  user = SearchUser(mail)
  if user is not None and password == user.password:
    print('Logged in!')
    return user
  else:
    print('error')

def SearchUser(mail):
  user = session.query(User).filter_by(email = mail).first()
  return user

def queryAll():
  users = session.query(User).all()
  if len(users) == 0:
    print("No users in the database")
    return
  return users

#def DescribeUser(user):
  #username = user.username
 # #password = user.password
  ##email = user.email
  ##print("User # {id}")
  #print(" Username: " + username)
  #print(" Password: " + password)
  ##print(" Email: " + email)