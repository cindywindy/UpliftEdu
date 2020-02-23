#pip install flask, flask-wtf, sqlalchemy, pyodbc
# import os
#import urllib.parse 
from flask import Flask, render_template
from donatorForm import DonorSignUp
#from flask_sqlalchemy import sqlalchemy
#params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=upliftedu.database.windows.net;DATABASE=pythonSQL;UID=Hack2020;PWD=UpliftEdu1")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'upliftedu'

#app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#db = sqlalchemy(app)

@app.route('/')
def home():
    return 'Welcome'

@app.route('/donorProfile')
def profile():
    return render_template('profile.html')

@app.route('/donorSignUp')
def donorSignUp():
    form = DonorSignUp()
    return render_template('DonorSignUp.html', form=form)

if __name__ == '__main__':
    app.run()