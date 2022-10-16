# Python
import pickle
from typing import Dict

# Pydantic
from pydantic import BaseModel, Field

# FastAPI
from fastapi import FastAPI
from fastapi import Body, Path

app = FastAPI()


# Models

class objectOne(BaseModel):
    p_temp: int = Field(..., example=268)
    batt_volt_value: int = Field(..., example=224)
    water_level: int = Field(..., example=115)

#class formatOne(BaseModel): 
#    f_tag: str = Field(..., example="PTemp")
#    f_type: str = Field(..., example="BattVolt.value")
#    f_len: int = Field(..., gt=0, example=12)


def encode(object: objectOne, format: Dict):
    pass

def decode():
    pass


@app.get("/")
def home():
    return {"Hello": "Tesacom"}

@app.get("/decode")
def get_decode(buffer):
    pass

@app.post("/encode")
def post_encode(object: objectOne=Body(...)):
    #
    format_one = [
        { "tag": "PTemp", "type": "int", len: 12 },
        { "tag": "BattVolt.value", "type": "int", len: 12 },
        { "tag": "WaterLevel", "type": "int", len: 8 }
        ]
    pass