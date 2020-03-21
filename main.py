from dotenv import load_dotenv
from os import getenv, path
from modules.grpc_server import StormGrpcService
from modules.rest_server import StormRestServer

if __name__ == '__main__':
    load_dotenv(path.join(path.dirname(__file__), '.env'))

    # StormRestServer.serve()
    StormGrpcService.serve()
