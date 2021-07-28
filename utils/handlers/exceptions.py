import collections

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's celery exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        data = response.data

        if not isinstance(data, dict):
            data = {
                'erro': data
            }
        response.data = {}
        errors = flatten_errors(data)
        response.data['errors'] = errors
        response.data['status'] = response.status_code

        response.data['exception'] = str(exc)

    return response


def flatten_errors(listum, key=''):
    items = []
    for k, v in listum.items():
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten_errors(v, k).items())
        else:
            items.append((k, v))
    return dict(items)
