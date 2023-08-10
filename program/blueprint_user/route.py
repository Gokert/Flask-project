import os

from flask import Blueprint, request, render_template, current_app, session
from db_work import select_dict, insert
from access import group_required
from paginator import pagination
from sql_provider import SQLProvider
from blueprint_user.forms import VacancyUserForm

blueprint_personal_account = Blueprint('personal_account_user', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_personal_account.route('/', methods=['GET', 'POST'])
@group_required
def personal_account():
    if request.method == 'GET':
        return render_template('user_header.html')
    elif request.method == 'POST':
        form = VacancyUserForm()

        name = form.name.data
        address = form.address.data
        gender = form.gender.data
        education = form.education.data
        birthday = form.birthday.data
        resume = form.resume.data

        insert(current_app.config["db_config"],
               provider.get("add_candidate.sql", Name=name, Address=address, Gender=gender, Education=education,
                            Birthday=birthday, resume=resume, user_id=session['user_id']))
        id = select_dict(current_app.config["db_config"],
                         provider.get("select_candidate.sql", Name=name, Birthday=birthday, Address=address, Gender=gender, Education=education))
        insert(current_app.config["db_config"],
               provider.get("add_interview.sql", Cand_id=id[0]['Cand_id'], Vac_id=session['vacancy_id']))

        session.pop("vacancy_id", None)

        return render_template('user_header.html')


@blueprint_personal_account.route('/vacancy_user', methods=['GET'])
def vacancy_user():
    limit = 5
    result = pagination(limit, provider, 'count_vacancy.sql', 'all_vacancy.sql')
    return render_template('vacancy_user.html', array=result['array'], page=result['page'],
                           total_pages=result['total_pages'])


@blueprint_personal_account.route('/resume/<int:id>', methods=['GET'])
def resume(id):
    session['vacancy_id'] = id
    form = VacancyUserForm()
    return render_template('resume.html', form=form)


@blueprint_personal_account.route('/results', methods=['GET'])
def results():
    limit = 10
    result = pagination(limit, provider, 'count_interview_user.sql', 'interview_user.sql', id=session['user_id'])
    return render_template('results.html', array=result['array'], page=result['page'],
                           total_pages=result['total_pages'])
