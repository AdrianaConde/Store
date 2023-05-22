from ..models.Tables import Supplier, Product, Order, Client
from pyramid.response import Response
from sqlalchemy import select
from pyramid.view import view_config
from .utils import parse
import json
from .database.get_conection import get_session
session = get_session()


@view_config(route_name='createSupplier',
             request_method='POST',
             renderer='json')
def createSupplier(request):
    print(request)
    supplier = parse(Supplier, request.body)
    session.add(supplier)
    session.commit()
    return Response(status=200)


@view_config(route_name='getSupplier',
             request_method='GET',
             renderer='json')
def getSupplier(request):
    idSupplier = request.matchdict['id']
    supplier_sentence = select(Supplier).where(
        Supplier.id == idSupplier)
    supplier = session.scalar(supplier_sentence)
    print('result', supplier.parseJson())
    supplier_json = json.dumps(supplier.parseJson()).encode()
    return Response(status=200, body=supplier_json, content_type='application/json')


@view_config(route_name='getSupplierDNI',
             request_method='GET',
             renderer='json')
def getSupplierDNI(request):
    idSupplier = request.matchdict['cedula']
    supplier_sentence = select(Supplier).where(
        Supplier.cedula == idSupplier)
    client_sentence = select(Client).where(Client.cedula == idSupplier)
    supplier = session.scalar(supplier_sentence)
    if (not supplier is None):
        supplier_json = json.dumps(supplier.parseJson()).encode()
        return Response(status=200, body=supplier_json, content_type='application/json')
    else:
        print('Cliente search')
        client = session.scalar(client_sentence)
        if (not client is None):
            client_json = json.dumps(client.parseJson()).encode()
            return Response(status=200, body=client_json, content_type='application/json')
        else:
            return Response(status=400)
