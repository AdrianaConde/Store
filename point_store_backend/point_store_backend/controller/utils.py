import json
from pyramid.response import Response
from pyramid.view import view_config


def parse(cls, json_data, ignore=[]):
    data = json.loads(json_data)
    instance = cls()
    for value in ignore:
        data.pop(value)
    for key, value in data.items():
        setattr(instance, key, value)

    return instance


@view_config(route_name='createSupplier', request_method='OPTIONS')
@view_config(route_name='createClient', request_method='OPTIONS')
@view_config(route_name='createOrder', request_method='OPTIONS')
@view_config(route_name='createProduct', request_method='OPTIONS')
@view_config(route_name='getSupplier', request_method='OPTIONS')
@view_config(route_name='getProduct', request_method='OPTIONS')
def options_handler(request):
    response = Response()
    response.headers.update({
        'Access-Control-Allow-Origin': 'http://localhost:4200',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    })
    return response
