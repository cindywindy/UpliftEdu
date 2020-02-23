from flask import Flask
from forms import SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'upliftedu'

@app.route('/')
def home():
    return 'Hello World'

@app.route('/profile/<int:profile_id>')
def profile(profile_id):
    return 'Profile number: ' + str(profile_id)

@approute('/donorSignUp'):
def donorSignUp():
    form = SignUpForm()
    return render_template('DonorSignUp.html, form=form')

if __name__ == '__main__':
    app.run()

