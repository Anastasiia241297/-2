from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import grpc
from auth_pb2 import AuthRequest
from score_pb2 import ScoreRequest
import auth_pb2_grpc
import score_pb2_grpc


app = FastAPI()
THRESHOLD_SCORE = 0.5  # Порог для пропуска


class CompositionRequest(BaseModel):
    login: str
    password: str


@app.post("/composition")
async def composition(request: CompositionRequest):
    # Взаимодействие с gRPC-сервисом score
    async with grpc.aio.insecure_channel("localhost:50052") as score_channel:
        score_stub = score_pb2_grpc.ScoreServiceStub(score_channel)
        score_response = await score_stub.GetScore(ScoreRequest(login=request.login))
        if score_response.score < THRESHOLD_SCORE:
            return {"can_enter": False}

    # Взаимодействие с gRPC-сервисом auth
    async with grpc.aio.insecure_channel("localhost:50051") as auth_channel:
        auth_stub = auth_pb2_grpc.AuthServiceStub(auth_channel)
        auth_response = await auth_stub.Authenticate(AuthRequest(login=request.login, password=request.password))
        if not auth_response.can_enter:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return {"can_enter": True}


