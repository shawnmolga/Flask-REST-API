from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><head></head><body><p>You truely are</p><img src="https://media1.tenor.com/images/b23a908ae01021bc1064937bad061b11/tenor.gif"></img></body></html>'


app.config['SERVER_NAME'] = 'hyver-security.com'
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=443, ssl_context='adhoc')
