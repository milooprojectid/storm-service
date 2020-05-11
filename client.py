from __future__ import print_function
import logging
import grpc
import modules.protobuf.storm_pb2 as storm_pb2
import modules.protobuf.storm_pb2_grpc as storm_pb2_grpc

def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = storm_pb2_grpc.StormServiceStub(channel)
        # response = stub.Summarize(storm_pb2.SummarizeRequest(text='https://kumparan.com/kumparanbisnis/sri-mulyani-tambah-anggaran-corona-rp-62-t-kpk-ancam-hukum-mati-jika-dikorupsi-1t49W501X86'))
        response = stub.HadistRetrieval(storm_pb2.HadistRequest(text='anak'))
        
        for hadist in response.hadists:
            print(hadist.text + '\n')


if __name__ == '__main__':
    logging.basicConfig()
    run()