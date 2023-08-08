import os

from flask import Blueprint, request, render_template, current_app, redirect, url_for
from db_work import select_dict,insert,delete
from access import group_required
from paginator import paginagion
from sql_provider import SQLProvider

blueprint_employees = Blueprint('employees', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_employees.route('/',methods=['GET','POST'])
@group_required
def empls():
        if request.method == 'GET':
            limit = 10
            result = paginagion(limit, provider, 'count_employees.sql', 'all_internal_users.sql')
            return render_template('empls_new.html',  array=result['array'], page=result['page'], total_pages=result['total_pages'])

@blueprint_employees.route('/<int:Emp_id>/del')
@group_required
def dl(Emp_id):
        delete(current_app.config['db_config'],provider.get("delete_employee.sql",Emp_id=Emp_id))
        return redirect(url_for('employees.empls'))

@blueprint_employees.route('/add/',methods=['GET','POST'])
@group_required
def add_empl():
        if request.method == 'GET':
            pos = select_dict(current_app.config['db_config'],provider.get('show_employees.sql'))
            return render_template('add_emp.html',positions=pos)

        elif request.method == 'POST':
            name = request.form.get('name_text')
            birthday = request.form.get('birthday_text')
            address = request.form.get('address_text')
            education= request.form.get('education_text')
            enroll_date = request.form.get('date_enroll_text')
            salary = request.form.get('salary_text')
            position1 = request.form.get('position_text')
            position2 = request.form.get('agent_id')

            str=[]
            if position2 == None:
                str = select_dict(current_app.config['db_config'],provider.get('find_position_name.sql',name_pos=position1));
                if len(str) ==0:
                    insert(current_app.config['db_config'],provider.get('add_position.sql', Name_pos=position1, Min=int(salary), Max=int(salary)))
                    str1 = select_dict(current_app.config['db_config'], provider.get('find_position_name.sql', name_pos=position1))[0]['Pos_id']
                else:
                    str1 = str[0]['Pos_id']
            else:
                position1=position2
                str1=select_dict(current_app.config['db_config'],provider.get('find_position_name.sql',name_pos=position1))[0]['Pos_id']

            insert(current_app.config['db_config'],provider.get('add_employees.sql',
            birthday=birthday,address=address,education=education,enroll_date=enroll_date,
            salary=salary,
            nm=name,
            position = str1 ))

            pos = select_dict(current_app.config['db_config'], provider.get('show_employees.sql'));
            #return render_template('add_emp.html',positions=pos)
            return redirect(url_for('employees.add_empl'))