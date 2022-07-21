from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# simple hello
@app.get('/hello/{name}')
async def hello(name):
    return f"Hello fast api {name}"


# get foods
class availableFoods(str, Enum):    
    gujrati= "gujrati"
    punjabi= "punjabi"

food_items = {
    "gujrati": ['fafda', "khaman" ],
    "punjabi": ['bhurji', "khimo" ]
}

@app.get('/get_items/{cuisine}')
async def cuisine_items(cuisine: availableFoods):
    return food_items.get(cuisine)


# coupon code to check against string input
available_coupons = {
    1: "10%",
    2: "20%",
    3: "30%",
}

@app.get('/get_coupon/{coupon}')
async def get_coupon(coupon_code: int):
    return available_coupons.get(coupon_code)