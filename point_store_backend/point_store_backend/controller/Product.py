from ..models.Tables import Product
from sqlalchemy import select
from pyramid.response import Response
from pyramid.view import view_config
from .utils import parse
import json
from .database.get_conection import get_session
session = get_session()


@view_config(route_name='createProduct',
             request_method='POST',
             renderer='json')
def createProduct(request):
    product = parse(Product, request.body)
    session.add(product)
    session.commit()
    return Response(status=200)


@view_config(route_name='getProduct',
             request_method='GET',
             renderer='json')
def getProduct(request):
    product_sentence = select(Product)
    product = session.scalars(product_sentence)
    prod = []
    for p in product:
        prod.append(p.parseJson())
    return Response(status=200, body=json.dumps(prod).encode(), content_type='application/json')
