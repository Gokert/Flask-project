import os
from flask import Blueprint, render_template, session, redirect, url_for
from sql_provider import SQLProvider

blueprint_admin = Blueprint('admin', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_admin.route('/', methods=['GET'])
def admin():
    if session.get('user_group') != None:
        return render_template('admin_all.html')
    else:
        return redirect(url_for("personal_account_user.personal_account"))
