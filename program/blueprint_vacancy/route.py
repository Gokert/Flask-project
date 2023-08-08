import datetime
import os

from flask import Blueprint, request, render_template, current_app, redirect, url_for
from db_work import select_dict,insert,delete
from access import group_required
from paginator import paginagion
from sql_provider import SQLProvider

blueprint_vacancy = Blueprint('vacancy', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_vacancy.route('/',methods=['GET','POST'])
@group_required
def vac():
        limit = 10
        result = paginagion(limit, provider, "count_vacancy.sql", "all_vacancy.sql")
        return render_template('vacancy.html', array=result['array'], page=result['page'], total_pages=result['total_pages'])

@blueprint_vacancy.route('/add',methods=['POST'])
@group_required
def vacancy_add():
        head = request.form.get('vacancy_heading')
        text = request.form.get('vacancy_text')
        salary = int(request.form.get('vacancy_salary'))
        dt_now = datetime.datetime.now()

        pos = select_dict(current_app.config['db_config'], provider.get('find_positions.sql', Name_pos=head))
        if (pos):
            insert(current_app.config['db_config'],provider.get("insert_vacancy.sql", Name=head, txt=text, Open_date=str(dt_now).split()[0]))
            return redirect(url_for('vacancy.vac'))

        insert(current_app.config['db_config'],provider.get('insert_position.sql',Name_pos=head,Min=salary,Max=salary))
        insert(current_app.config['db_config'],provider.get("insert_vacancy.sql",Name=head,txt=text,Open_date=str(dt_now).split()[0]))
        return redirect(url_for('vacancy.vac'))

@blueprint_vacancy.route('/<int:vacancy_id>/del')
@group_required
def dlt(vacancy_id):
        delete(
            current_app.config['db_config'],provider.get("delete.sql",vacancy_id=vacancy_id)
        )
        return redirect(url_for('vacancy.vac'))
