from pyramid.response import Response
from pyramid.view import view_config


@view_config(
    route_name='home'
)
def home(request):
    return Response('Welcome!')


def includeme(config):
    config.add_route('home', '/')
    config.add_route('createClient', '/createClient')
    config.add_route('createProduct', '/createProduct')
    config.add_route('createOrder', '/createOrder')
    config.add_route('createSupplier', '/createSupplier')
    config.add_route('getSupplier', '/getSupplier/{id}')
    config.add_route('getProduct', '/getProduct')
    config.add_route('getClient', '/getClient/{id}')
    config.add_route('getSupplierDNI', '/getSupplierDNI/{cedula}')
