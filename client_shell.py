import urllib3
import requests
import json


login_url = 'http://127.0.0.1:5000/login'
api_url = 'http://127.0.0.1:5000/api/bindings'

while True:
    username = input("Please enter username: ")
    password = input("Please enter password: ")

    auth = username+':'+password
    head = urllib3.util.make_headers(basic_auth=auth)
    status = 0
    r = None
    try:
        r = requests.get(login_url, verify=False, headers=head)
        status = r.status_code
    except:
        print('error accessing API')
        exit();
    if status == 401:
        print("wrong username or password. please try again\n")
    else:
        if status == 200:
            break
        else:
            print('something went wrong. exiting')
            exit()

r_jsonified = r.json()
token = r_jsonified['token']

#we have successfullly received a token
#now we enter the API

try:
    with open('to_upload.json') as f:
        try:
            data = json.load(f)
        except ValueError as e:
            print('wrong file format. exiting')
            exit()
except:
    print('error opening file. exiting')
    exit()


head = {'x-access-token': token, 'content-type': 'application/json'}
response = requests.post(api_url, data=json.dumps(data),headers=head)

try:
    with open('ouput.json', 'w') as outfile:
        json.dump(response.json(), outfile, ensure_ascii=False)
except:
    print('error opening output file. exiting')
    exit()