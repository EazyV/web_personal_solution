from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from . import BitrixClient
from starlette.status import HTTP_204_NO_CONTENT
import json
import re

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def read_root():
    return HTMLResponse(content=open('static/index.html', 'r', encoding="utf_8").read(), media_type='text/html')


with open('app/tok.json', 'r') as file:
    data = json.load(file)
user = BitrixClient(data["token"])


@app.post("/message_applicant")
async def register(applicant_name=Form(), applicant_phone=Form()):
    lead_data = {
        "fields":
            {"TITLE": "Новый лид Соискатель",
             "NAME": applicant_name,
             "PHONE": [{"VALUE": applicant_phone, "VALUE_TYPE": "WORK"}],
             "SOURCE_ID": "WEBFORM",
             "ASSIGNED_BY_ID": 1}}
    user.create_lead(lead_data)
    raise HTTPException(status_code=HTTP_204_NO_CONTENT)


@app.post("/message_customer")
async def register(customer_email=Form(), customer_name=Form(), customer_phone=Form()):
    lead_data = {
        "fields": {
            "TITLE": "Новый лид Заказчик",
            "NAME": customer_name,
            "PHONE": [{"VALUE": customer_phone, "VALUE_TYPE": "WORK"}],
            "SOURCE_ID": "WEBFORM",
            "ASSIGNED_BY_ID": 1
        }
    }

    if customer_email and not customer_email.isspace() and re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$',
                                                                    customer_email):
        lead_data["fields"]["EMAIL"] = [{"VALUE": customer_email, "VALUE_TYPE": "WORK"}]

    user.create_lead(lead_data)
    raise HTTPException(status_code=HTTP_204_NO_CONTENT)
