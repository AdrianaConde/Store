from ..models.Tables import Order, association_table, Product
from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy import select
from .utils import parse
import json
from .database.get_conection import get_session
session = get_session()
#amount, client, product, supplier, array: products_id
@view_config(route_name='createOrder',
            request_method='POST', 
            renderer= 'json')

def createOrder(request):
    order =  parse(Order, request.body, ignore=['products'])
    idsProduct =  json.loads(request.body)['products']
    print(idsProduct)
    product_sentence =  select(Product).where(Product.id.in_(idsProduct))
    product = session.scalars(product_sentence)
    order.products.extend(product)
    session.add(order)
    session.commit()

    return Response(status=200)