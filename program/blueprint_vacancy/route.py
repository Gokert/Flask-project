import datetime
import os

from flask import Blueprint, render_template, current_app, redirect, url_for, request
from db_work import select_dict, insert, delete
from access import group_required
from paginator import pagination
from sql_provider import SQLProvider
from blueprint_vacancy.forms import VacancyAddForm

blueprint_vacancy = Blueprint('vacancy', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_vacancy.route('/', methods=['GET'])
@group_required
def vacancy():
    limit = 10
    result = pagination(limit, provider, "count_vacancy.sql", "all_vacancy.sql")
    form = VacancyAddForm()
    return render_template('vacancy.html', array=result['array'], page=result['page'],
                           total_pages=result['total_pages'], form=form)


@blueprint_vacancy.route('/add', methods=['POST'])
@group_required
def vacancy_add():
    form = VacancyAddForm()
    head = form.head.data
    text = form.text.data
    salary = form.salary.data

    dt_now = datetime.datetime.now()

    position_id = select_dict(current_app.config['db_config'], provider.get('find_positions.sql', Name_pos=head))
    if position_id:
        insert(current_app.config['db_config'],
               provider.get("insert_vacancy.sql", Name=head, txt=text, Open_date=str(dt_now).split()[0], Pos_id=position_id[0]['Pos_id']))
        return redirect(url_for('vacancy.vacancy'))

    insert(current_app.config['db_config'], provider.get('insert_position.sql', Name_pos=head, Min=salary, Max=salary))

    position_id = select_dict(current_app.config['db_config'], provider.get('find_positions.sql', Name_pos=head))

    insert(current_app.config['db_config'],
    provider.get("insert_vacancy.sql", Name=head, txt=text, Open_date=str(dt_now).split()[0], Pos_id=position_id[0]['Pos_id']))

    return redirect(url_for('vacancy.vacancy'))


@blueprint_vacancy.route('/<int:vacancy_id>/del', methods=['GET'])
@group_required
def delete_vacancy(vacancy_id):
    delete(
        current_app.config['db_config'], provider.get("delete.sql", vacancy_id=vacancy_id)
    )
    return redirect(url_for('vacancy.vacancy'))
