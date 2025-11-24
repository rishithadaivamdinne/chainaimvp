from fastapi import FastAPI, UploadFile, File
import pandas as pd
from agent.basicagent import moving_average_forecast, recommend_order

app = FastAPI()

@app.post("/recommend")
async def recommend(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(pd.io.common.BytesIO(contents))
    forecast = moving_average_forecast(df, window=4)
    recommendation = recommend_order(forecast, safety_factor=1.1)
    return {
        "forecast": round(forecast, 2),
        "recommended_order": recommendation
    }
