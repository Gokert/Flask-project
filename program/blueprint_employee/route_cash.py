import os

from flask import Blueprint, render_template, request, current_app, session, redirect, url_for

from access import group_required
from db_context_manager import DBContextManager

from db_work import select_dict
from sql_provider import SQLProvider
from cache.wrapper import fetch_from_cache

blueprint_employees = Blueprint('blueprint_employee', __name__, template_folder='templates', static_folder='static')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_employees.route('/',methods=['GET','POST'])
@group_required
def empls():
    print("CACHE")
    array = select_dict(current_app.config['db_config'], provider.get("all_internal_users.sql"))

    db_config = current_app.config['db_config']
    cashe_config = current_app.config['cache_config']
    cached_select = fetch_from_cache('all_items_cached', cashe_config)(select_dict)
    print('cashed_select=', cashe_config)

    return render_template('empls.html', array=array)

    """
    db_config = current_app.config['db_config']
    cashe_config = current_app.config['cashe_config']
    cached_select = fetch_from_cache('all_items_cached', cashe_config)(select_dict)
    print('cashed_select=', cashe_config)
    if request.method == 'GET':
        sql = provider.get('all_items.sql')
        items = cached_select(db_config, sql)
        basket_items = session.get('basket', {})
        return render_template('basket_order_list.html', items=items, basket=basket_items)
    else:
        prod_id = request.form['prod_id']
        sql = provider.get('select_item.sql', prod_id=prod_id)
        item = select_dict(db_config, sql)[0]

        add_to_basket(prod_id, item)

        return redirect(url_for('bp_order.order_index'))"""

"""
@blueprint_order.route('/save_order', methods=['GET', 'POST'])
@group_required
def save_order():
    user_id = session.get('user_id')
    current_basket = session.get('basket', {})
    order_id = save_order_with_list(current_app.config['db_config'], user_id, current_basket)
    if order_id:
        session.pop('basket')
        return render_template('order_created.html', order_id=order_id)
    else:
        return 'Что-то пошло не так'


@group_required
def save_order_with_list(dbconfig: dict, user_id: int, current_basket: dict):
    with DBContextManager(dbconfig) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        _sql1 = provider.get('insert_order.sql', user_id=user_id, order_date='2022-11-01')
        result1 = cursor.execute(_sql1)
        if result1 == 1:
            _sql2 = provider.get('select_order_id.sql', user_id=user_id)
            cursor.execute(_sql2)
            order_id = cursor.fetchall()[0][0]
            print('order_id=', order_id)
            if order_id:
                for key in current_basket:
                    print(key, current_basket[key]['amount'])
                    prod_amount = current_basket[key]['amount']
                    _sql3 = provider.get('insert_order_list.sql', order_id=order_id, prod_id=key,
                                         prod_amount=prod_amount)
                    cursor.execute(_sql3)
                return order_id


@blueprint_order.route('/clear-basket')
@group_required
def clear_basket():
    if 'basket' in session:
        session.pop('basket')
    return redirect(url_for('bp_order.order_index'))
"""
@blueprint_employees.route('/<int:Emp_id>/del')
@group_required
def dl(Emp_id):
        delete(current_app.config['db_config'],provider.get("delete_employee.sql",Emp_id=Emp_id))
        return redirect(url_for('blueprint_employee.empls'))

@blueprint_employees.route('/add/',methods=['GET','POST'])
@group_required
def add_empl():
        if request.method=='GET':
            pos = select_dict(current_app.config['db_config'],provider.get('show_employees.sql'));
            return render_template('add_emp.html',positions=pos)

        elif request.method=='POST':
            name = request.form.get('name_text')
            birthday = request.form.get('birthday_text')
            address = request.form.get('address_text')
            education= request.form.get('education_text')
            enroll_date = request.form.get('date_enroll_text')
            salary = request.form.get('salary_text')
            position1 = request.form.get('position_text')
            position2 = request.form.get('agent_id')

            str=[]
            print(position2)
            if position2 == None:
                str = select_dict(current_app.config['db_config'],provider.get('find_position_name.sql',name_pos=position1));
                if len(str) ==0:
                    insert(current_app.config['db_config'],provider.get('add_position.sql', Name_pos=position1, Min=int(salary) - 10000, Max=int(salary) + 10000))
                    str = select_dict(current_app.config['db_config'], provider.get('find_position_name.sql', name_pos=position1))[0]['Pos_id']
                else:
                    print(str)
                    str = str[0]['Pos_id']
            else:
                position1=position2
                str=select_dict(current_app.config['db_config'],provider.get('find_position_name.sql',name_pos=position1))[0]['Pos_id']

            insert(current_app.config['db_config'],provider.get('add_employees.sql',
            birthday=birthday,address=address,education=education,enroll_date=enroll_date,
            salary=salary,nm=name,position=str))

            pos = select_dict(current_app.config['db_config'], provider.get('show_employees.sql'));
            return render_template('add_emp.html',positions=pos)