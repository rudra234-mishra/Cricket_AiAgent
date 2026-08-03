from logging_config import logger
from fastapi import FastAPI
from pydantic import BaseModel,Field
from graph import build_graph
from model import database_conn
import json

app = FastAPI()

pipeline = build_graph()

@app.get('/')
def home():
    return 'Agent Running :'

    
class Request(BaseModel):
    name: str

@app.post("/runs")
def runs(req: Request):

    result = pipeline.invoke({"Name": req.name})

    conn = database_conn()
    cur = conn.cursor()

    query = """
    INSERT INTO "Rudra"."player_stat"
    ("Name","Odi","T20","Test","Ipl","Summary")
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cur.execute(
        query,
        (
            result["Name"],
            json.dumps(result["ODI"]),
            json.dumps(result["T20"]),
            json.dumps(result["TEST"]),
            json.dumps(result["IPL"]),
            result["Summary"],
        ),
    )

    conn.commit()
    cur.close()
    conn.close()

    return result