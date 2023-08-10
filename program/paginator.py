from flask import current_app, request
from db_work import select_dict


def pagination(limit=10, provider=None, count_sql_script=None, sql_script=None, id=None):
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * limit
    count = select_dict(current_app.config['db_config'], provider.get(count_sql_script, id=id))
    total_pages = int(count[0]["count(*)"] / limit) + (count[0]["count(*)"] % limit > 0)

    array = select_dict(current_app.config['db_config'],
                        provider.get(sql_script, limit=limit, offset=offset, id=id))

    results = {'array': array, "page": page, "total_pages": total_pages}

    return results
