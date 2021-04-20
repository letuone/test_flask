from flask import Flask,escape
app=Flask(__name__)

@app.route('/')
def hello_world():
    username=request.args.get('name','Flask')
    return 'Hello, %s!' % escape(username)
    