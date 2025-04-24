from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse

## Extra Library
import numpy as np
import pandas as pd

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/material_comp")
def material_comp():
    df_compositions = pd.read_excel(open('assets/new_comp_fat_snf_prot_lac.xlsx', 'rb'), sheet_name='compo')
    df_compositions = df_compositions.set_index('ingridient')
    data = df_compositions.reset_index().to_dict(orient='records')
    return data

@app.get("/recipies")
def recipies():
    df_recepies = pd.read_excel(open('assets/new_comp_fat_snf_prot_lac.xlsx', 'rb'), sheet_name='target')
    df_recepies = df_recepies.set_index('receipe')
    data = df_recepies.reset_index().to_dict(orient='records')
    return data