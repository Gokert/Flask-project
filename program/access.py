from functools import wraps
from flask import session, render_template, request, current_app


def login_required(func):
    """Authorization verification"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        return render_template("main_header.html")

    return wrapper


def group_validation(config: dict) -> bool:
    endpoint_func = request.endpoint
    endpoint_app = request.endpoint.split('.')[0]
    if 'user_group' in session:
        user_group = session['user_group']
        if user_group is None:
            user_group = 'external'
        if user_group in config and endpoint_app in config[user_group]:
            return True
        elif user_group in config and endpoint_func in config[user_group]:
            return True
    return False


def group_required(f):
    """Rights verification"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        config = current_app.config['access_config']
        if group_validation(config):
            return f(*args, **kwargs)
        return "You have no rights!"

    return wrapper
