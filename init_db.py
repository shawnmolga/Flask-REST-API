from my_api import db, User
from werkzeug.security import generate_password_hash
import uuid


def init_db():
    print('Initializing user database and creating one admin user for testing purposes.\nUsername = admin, Password = password')
    db.create_all()
    hashed_password = generate_password_hash('password', method='sha256')
    new_user = User(public_id=str(uuid.uuid4()), username='admin', password=hashed_password)
    db.session.add(new_user)
    db.session.commit()


def create_new_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user:
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(public_id=str(uuid.uuid4()), username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
    else:
        print('User already exists. Please try again.')

if __name__ == '__main__':
    init_db()
    while True:
        cont = input('Would you like to create a new user? Y N')
        if cont == 'N':
            break
        else:
            if cont == 'Y':
                username = input("Please enter username: ")
                password = input("Please enter password: ")
                create_new_user(username, password)

