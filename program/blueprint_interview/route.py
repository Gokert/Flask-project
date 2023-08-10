import os

from flask import Blueprint, request, render_template, current_app, redirect, url_for, session
from db_work import select_dict, insert
from access import group_required
from paginator import pagination
from sql_provider import SQLProvider
from blueprint_interview.forms import EditInterviewForm

blueprint_interview = Blueprint('interview', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_interview.route('/', methods=['GET', 'POST'])
@group_required
def interview():
    limit = 10
    result = pagination(limit, provider, "count_interview.sql", "all_interview.sql")
    if request.method == 'GET':
        return render_template('interview.html', array=result['array'], page=result['page'],
                               total_pages=result['total_pages'])
    elif request.method == "POST":
        form = EditInterviewForm()
        result = form.result.data
        scores = form.scores.data
        name_emp = request.form.get("agent_id")
        int_date = form.int_date.data

        insert(current_app.config['db_config'], provider.get("edit_interview.sql", Result=result,
                                                             Scores=scores,
                                                             Name_emp=name_emp,
                                                             Int_date=int_date,
                                                             Int_id=session["interview_id"])
               )

        session.pop("interview_id", None)
        return redirect(url_for('interview.interview'))


@blueprint_interview.route('/edit/<int:Int_id>', methods=['GET', 'POST'])
@group_required
def edit_interview(Int_id):
    if request.method == "GET":
        session["interview_id"] = Int_id
        form = EditInterviewForm()

        all_employees = select_dict(current_app.config['db_config'], provider.get("all_employees.sql"))
        last_interview = select_dict(current_app.config['db_config'], provider.get("information_for_edit_interview.sql", Int_id=Int_id))[0]
        form.result.data = last_interview['Result']
        form.scores.data = last_interview['Scores']
        form.int_date.data = last_interview['Int_date']
        form.name_emp.data = last_interview['Name_emp']
        name_emp = last_interview['Name_emp']

        return render_template('interview_edit.html', Int_id=Int_id, form=form, array=all_employees, name_emp=name_emp)


@blueprint_interview.route('/new', methods=['GET', 'POST'])
def new_interview():
    if request.method == "GET":
        limit = 10
        result = pagination(limit, provider, "count_interview_occupied.sql", "interview_occupied.sql")

        return render_template("interview.html", array=result['array'], page=result['page'],
                               total_pages=result['total_pages'])


@blueprint_interview.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "GET":
        limit = 10
        result = pagination(limit, provider, "count_interview_unoccupied.sql", "interview_unoccupied.sql")
        return render_template('interview.html', array=result['array'], page=result['page'],
                               total_pages=result['total_pages'])


@blueprint_interview.route('/show/<int:Int_id>', methods=['GET', 'POST'])
def show_candidate(Int_id):
    if request.method == 'GET':
        array = select_dict(current_app.config['db_config'], provider.get("find_candidate.sql", Int_id=Int_id))
        return render_template('show_candidate.html', array=array)
