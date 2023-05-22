import argparse
import dotenv
import os
from point_store_backend.server import serve
from point_store_backend.controller.database.get_conection import get_engine
from wsgiref.simple_server import make_server
from point_store_backend.models.Meta import Base
from point_store_backend.models.Tables import *


def start_server():
    print(f"Start server on {os.getenv('HOST')}:{os.getenv('PORT')}")
    app = serve({})
    server = make_server(os.getenv('HOST'), int(os.getenv('PORT')), app)
    server.serve_forever()


def migrate_database():
    print("Migrate Database")
    engine = get_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['startserver', 'migrate'])
    args = parser.parse_args()
    dotenv.load_dotenv()
    if args.command == 'startserver':
        start_server()
    elif args.command == 'migrate':
        migrate_database()
    else:
        print('Commando not found')


if __name__ == '__main__':
    main()
