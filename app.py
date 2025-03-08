import os
import uvicorn
from fastapi import FastAPI
from starlette.responses import Response
from starlette.responses import RedirectResponse
from src.stages.Prediction import PredictionPipeline


app = FastAPI()


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python -B main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predict_route(text: str):
    try:
        obj = PredictionPipeline()
        result = obj.predict(text)
        return {"summary": result}
    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
