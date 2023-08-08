import os

from flask import Blueprint, request, render_template, current_app, redirect, url_for
from db_work import select_dict, insert, call_proc
from access import group_required
from paginator import paginagion
from sql_provider import SQLProvider

blueprint_interview = Blueprint('interview', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

buf = {'Int_id': None}

@blueprint_interview.route('/', methods=['GET', 'POST'])
@group_required
def interview():
    limit = 10
    result = paginagion(limit, provider, "count_interview.sql", "all_interview.sql")
    if request.method == 'GET':
        return render_template('interview.html', array=result['array'], page=result['page'], total_pages=result['total_pages'])

    elif request.method == "POST":
        Result = request.form.get("Result")
        Scores = request.form.get("Scores")
        Name_emp = request.form.get("agent_id")
        Int_date = request.form.get("Int_date")

        insert(current_app.config['db_config'], provider.get("edit_interview.sql", Result=Result,
                                                             Scores=Scores,
                                                             Name_emp=Name_emp,
                                                             Int_date=Int_date,
                                                             Int_id=buf['Int_id'])
               )
        # array = select_dict(current_app.config['db_config'], provider.get("all_interview.sql"))
        # buf['Int_id'] = None
        #
        # return render_template('interview.html', array=array)
        return redirect(url_for('interview.interview'))



@blueprint_interview.route('/edit/<int:Int_id>', methods=['GET', 'POST'])
@group_required
def edit(Int_id):
    if request.method == "GET":
        #array = select_dict(current_app.config['db_config'], provider.get("all_employees.sql"))
        buf['Int_id'] = Int_id
        return render_template('interview_edit.html', Int_id=Int_id)


@blueprint_interview.route('/report', methods=['GET', 'POST'])
def report():
    res = call_proc(current_app.config['db_config'], 'cand_report1', 11, 2020)
    if request.method == "GET":
        return render_template("report.html")
    elif request.method == "POST":
        start = request.form.get("start")
        end = request.form.get("end")
        array = select_dict(current_app.config['db_config'], provider.get("proc.sql", start=start, end=end))
        return render_template("interview.html", array=array)


@blueprint_interview.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == "GET":
        limit = 10
        result = paginagion(limit, provider, "count_interview_occupied.sql", "interview_occupied.sql")

        return render_template("interview.html", array=result['array'], page=result['page'], total_pages=result['total_pages'])


@blueprint_interview.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == "GET":
        limit = 10
        result = paginagion(limit, provider, "count_interview_unoccupied.sql", "interview_unoccupied.sql")

        return render_template('interview.html', array=result['array'], page=result['page'], total_pages=result['total_pages'])


@blueprint_interview.route('/show/<int:Int_id>', methods=['GET', 'POST'])
def show(Int_id):
    if request.method == 'GET':
        array = select_dict(current_app.config['db_config'], provider.get("find_candidate.sql", Int_id=Int_id))
        return render_template('show_candidate.html', array=array)


