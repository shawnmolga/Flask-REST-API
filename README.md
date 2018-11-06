
## Quick Start

### Basics

1. Make sure pip version is up to date
2. Install the requirements

```sh
$ pip install -r requirements.tst
```

### Create DB

Create the databases:

```sh
$ python init_db.py
```
The database is created with one table: User(public_id, username, password), 
and automatically inserts one tuple for the admin user (username=admin, password=password).
The init_db.py script will allow to insert new users if you wish.

### Run the Application

```sh
$ python server.py
$ python my_api.py
```
Access the application at the address [http://127.0.0.1:5000/]

###Shell Client
1. save the json file you would like to upload to the API in the current directory, 
    in the name "to_upload.json"
2. run:
```sh
$ python client_shell.py
```



### Testing



```sh
$ python my_unittest.py
$ python fetcher_unittest.py
```

