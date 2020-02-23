from flask import Flask, render_template
from donatorForm import DonorSignUp
app = Flask(__name__)
app.config['SECRET_KEY'] = 'upliftedu'

@app.route('/')
def home():
    return 'Welcome'

@app.route('/profile/<int:profile_id>')
def profile(profile_id):
    return 'Profile number: ' + str(profile_id)

@app.route('/donorSignUp')
def donorSignUp():
    form = DonorSignUp()
    return render_template('DonorSignUp.html', form=form)

if __name__ == '__main__':
    app.run()

