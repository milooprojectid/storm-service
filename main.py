from dotenv import load_dotenv
from os import getenv, path
from modules.server.grpc_server import StormGrpcService
from modules.server.rest_server import StormRestServer

if __name__ == '__main__':
    load_dotenv(path.join(path.dirname(__file__), '.env'))

    # StormRestServer.serve()
    StormGrpcService.serve()
