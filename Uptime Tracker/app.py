
from flask import render_template, redirect, request, url_for, flash,abort
from models import uptime
import os
from flask import Flask

app = Flask(__name__)
title=''
status='new'

@app.route('/')
def home():
    return render_template('index.html',errormsg="")
   

@app.route('/components',methods=['POST'])
def component():
    val_id=request.form['cred_id']
    val_pass=request.form['cred_pass']
    try:
        print(val_id)
        print(val_pass)
        uptime.beatstracker(val_id,val_pass)
    except:
        return render_template('index.html',errormsg="Please enter a valid Id Password")
    #logger.login(val_id,val_pass)
    return render_template('end.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
