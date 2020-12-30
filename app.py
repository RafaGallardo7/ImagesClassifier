from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/clasificar', methods=['GET','POST'])
def clasificar():    
    result = "CLASIFICAR"
    return result