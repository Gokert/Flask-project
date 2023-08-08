import os

from flask import Blueprint, request, render_template, current_app, session
from db_work import select_dict, insert
from access import group_required
from paginator import paginagion
from sql_provider import SQLProvider

blueprint_personal_account = Blueprint('personal_account_user', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

buf = {'Vac_id': None}

@blueprint_personal_account.route('/',methods=['GET','POST'])
@group_required
def personal_account():
    if request.method =='GET':
        return render_template('user_header.html')
    elif request.method=='POST':
        name = request.form.get("Name")
        address = request.form.get("Address")
        gender = request.form.get("Gender")
        education = request.form.get("Education")
        Birthday = request.form.get("Birthday")
        resume = request.form.get("resume")

        insert(current_app.config["db_config"],provider.get("add_candidate.sql", Name = name, Address=address, Gender=gender, Education=education, Birthday=Birthday, resume=resume, user_id=session['user_id']))
        id = select_dict(current_app.config["db_config"],provider.get("select_candidate.sql",Name=name,Birthday=Birthday))
        insert(current_app.config["db_config"],provider.get("add_interview.sql",Cand_id=id[0]['Cand_id'], Vac_id=buf['Vac_id']))

        buf['Vac_id']=None
        return render_template('user_header.html')

@blueprint_personal_account.route('/vacancy_user',methods=['GET','POST'])
def vacancy_user():
    limit = 5
    result = paginagion(limit, provider, 'count_vacancy.sql', 'all_vacancy.sql')
    return render_template('vacancy_user.html', array=result['array'], page=result['page'], total_pages=result['total_pages'])

@blueprint_personal_account.route('/resume/<int:id>',methods=['GET','POST'])
def resume(id):
    if request.method == 'GET':
        buf['Vac_id'] = id
        return render_template('resume.html')

@blueprint_personal_account.route('/results')
def results():
    limit = 10
    result = paginagion(limit, provider, 'count_interview_user.sql', 'interview_user.sql', id=session['user_id'])
    return render_template('results.html', array=result['array'], page=result['page'], total_pages=result['total_pages'])



