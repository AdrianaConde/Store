from pyramid.config import Configurator

from pyramid.events import NewRequest


def add_cors_headers(event):
    def cors_headers(request, response):
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)


def serve(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    print(settings)
    with Configurator(settings=settings) as config:
        # config.include('pyramid_jinja2')
        config.include('.controller.routes')
        config.add_subscriber(add_cors_headers, NewRequest)
        # config.include('.models')
        config.scan()
    return config.make_wsgi_app()
