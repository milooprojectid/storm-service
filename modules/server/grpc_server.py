import grpc
import modules.protobuf.storm_pb2_grpc as storm_grpc
import modules.protobuf.storm_pb2 as storm_pb

from concurrent import futures
from modules.summarization.summarization import summarization
from validators import url
from modules.summarization.news_link import getNews
from os import getenv

class StormGrpcService(storm_grpc.StormServiceServicer):
    def Summarize(self, request, context):
        text = request.text

        # if is a link, override value
        if (url(text)):
            text = getNews(text)

        summarizer = summarization()
        summary = summarizer.fit(text)
        return storm_pb.SummarizeResponse(summary=summary)
    
    @staticmethod
    def serve():
        port = getenv('GRPC_PORT') or '50051'
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        storm_grpc.add_StormServiceServicer_to_server(StormGrpcService(), server)
        server.add_insecure_port('[::]:'+str(port))
        server.start()
        print("serving grpc server at " + port)

        server.wait_for_termination()
