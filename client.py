from __future__ import print_function
import logging

import grpc

import modules.storm_pb2 as storm_pb2
import modules.storm_pb2_grpc as storm_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('127.0.0.1:6060') as channel:
        stub = storm_pb2_grpc.StormServiceStub(channel)
        response = stub.Summarize(storm_pb2.SummarizeRequest(text='https://kumparan.com/kumparanbisnis/sri-mulyani-tambah-anggaran-corona-rp-62-t-kpk-ancam-hukum-mati-jika-dikorupsi-1t49W501X86'))
    print("Greeter client received: " + response.summary)


if __name__ == '__main__':
    logging.basicConfig()
    run()