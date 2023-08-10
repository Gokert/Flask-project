import os

from flask import Blueprint, request, render_template, current_app, redirect, url_for
from db_work import select_dict, insert, delete
from access import group_required
from paginator import pagination
from sql_provider import SQLProvider
from blueprint_employee.forms import EmployeeAddForm

blueprint_employees = Blueprint('employees', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_employees.route('/', methods=['GET', 'POST'])
@group_required
def employees():
    if request.method == 'GET':
        limit = 10
        result = pagination(limit, provider, 'count_employees.sql', 'all_internal_users.sql')
        return render_template('employees.html', array=result['array'], page=result['page'],
                               total_pages=result['total_pages'])


@blueprint_employees.route('/<int:Emp_id>/del', methods=['GET'])
@group_required
def delete_employee(Emp_id):
    delete(current_app.config['db_config'], provider.get("delete_employee.sql", Emp_id=Emp_id))
    return redirect(url_for('employees.employees'))


@blueprint_employees.route('/add/', methods=['GET', 'POST'])
@group_required
def add_employee():
    form = EmployeeAddForm()
    if request.method == 'GET':
        pos = select_dict(current_app.config['db_config'], provider.get('show_employees.sql'))
        return render_template('add_employee.html', positions=pos, form=form)
    elif request.method == 'POST':
        name = form.name.data
        birthday = form.birthday.data
        address = form.address.data
        education = form.education.data
        enroll_date = form.enroll_date.data
        salary = form.salary.data
        position = request.form.get('agent_id')

        insert(current_app.config['db_config'], provider.get('add_employees.sql',
                                                             birthday=birthday, address=address, education=education,
                                                             enroll_date=enroll_date,
                                                             salary=salary,
                                                             nm=name,
                                                             position=position)
               )

        return redirect(url_for('employees.add_employee'))
