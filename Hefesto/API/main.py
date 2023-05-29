from fastapi import FastAPI, Response, status
import pandas as pd
import uvicorn
import os
from Hefesto.main import Hefesto

app = FastAPI()

@app.post("/hefesto-fiab")
async def upload_csv(response: Response):
    current_dir = os.getcwd()
    test = Hefesto(datainput = current_dir + "/data/CDE.csv")
    transform = test.transformFiab()
    transform.to_csv (current_dir + "/data/CDE_result.csv", index = False, header=True)
    response.status_code = status.HTTP_200_OK
    if response.status_code == 200:
        return {response.status_code:"Structural Transformation done"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)