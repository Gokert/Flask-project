from flask import Flask, render_template, json, session
from auth.route import blueprint_auth
from admin.route import blueprint_admin
from blueprint_employee.route import blueprint_employees
from blueprint_vacancy.route import blueprint_vacancy
from access import login_required
from blueprint_user.route import blueprint_personal_account
from blueprint_interview.route import blueprint_interview
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'Superley'
csrf = CSRFProtect()

app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_admin, url_prefix='/admin')
app.register_blueprint(blueprint_employees, url_prefix='/employees')
app.register_blueprint(blueprint_vacancy, url_prefix='/vacancy')
app.register_blueprint(blueprint_personal_account, url_prefix='/personal_account')
app.register_blueprint(blueprint_interview, url_prefix='/interview')

app.config['db_config'] = json.load(open('data_files/dbconfig.json'))
app.config['access_config'] = json.load(open('data_files/access.json'))


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@login_required
def menu_choice():
    """Home page"""

    if 'user_id' in session:
        if session.get('user_group', None):
            return render_template("main_header.html", username=session.get('username'))
        else:
            return render_template("main_header.html", username=session.get('username'))
    else:
        return render_template("main_header.html")


@app.route('/exit', methods=['GET'])
def exit_func():
    session.clear()
    return render_template("main_header.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
