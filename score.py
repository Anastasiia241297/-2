from concurrent import futures
import grpc
from score_pb2 import ScoreResponse
import score_pb2_grpc

class ScoreService(score_pb2_grpc.ScoreServiceServicer):
    def GetScore(self, request, context):
        return ScoreResponse(score=1.0)  # Fictitious value

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    score_pb2_grpc.add_ScoreServiceServicer_to_server(ScoreService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()





