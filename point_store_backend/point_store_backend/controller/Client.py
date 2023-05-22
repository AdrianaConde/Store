from ..models.Tables import Client, Order, Product
from sqlalchemy import select
from pyramid.response import Response
from pyramid.view import view_config
from .utils import parse
import json
from .database.get_conection import get_session
session = get_session()


@view_config(route_name='createClient',
             request_method='POST',
             renderer='json')
def createClient(request):
    client = parse(Client, request.body)
    add = session.add(client)
    commit = session.commit()
    print(client.id)
    return Response(status=200)


@view_config(route_name='getClient',
             request_method='GET',
             renderer='json')
def getClient(request):
    idClient = request.matchdict['id']
    client_sentence = select(Client).where(Client.id == idClient)
    client = session.scalar(client_sentence)
    client_json = json.dumps(client.parseJson()).encode()
    return Response(status=200, body=client_json, content_type='application/json')
