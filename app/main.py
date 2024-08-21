from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from . import BitrixClient
from starlette.status import HTTP_204_NO_CONTENT
from .models import ApplicantData, CustomerData
from pydantic import ValidationError
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def read_root():
    return HTMLResponse(content=open('static/index.html', 'r', encoding="utf_8").read(), media_type='text/html')


with open('app/tok.json', 'r') as file:
    data = json.load(file)
user = BitrixClient(data["token"])


@app.post("/message_applicant")
async def register_applicant(applicant_name=Form(), applicant_phone=Form()):
    try:
        applicant_data = ApplicantData(applicant_name=applicant_name, applicant_phone=applicant_phone)
    except ValidationError as e:
        # Обработка ошибки валидации
        error_messages = {error['loc'][0]: error['msg'] for error in e.errors()}
        if 'customer_email' in error_messages:
            raise HTTPException(status_code=400, detail="Неверный формат email.")
        logger.error(f"Ошибка валидации данных: {error_messages}")
        raise HTTPException(status_code=400, detail="Ошибка валидации данных.")
    lead_data = {
        "fields":
            {"TITLE": "Новый лид Соискатель",
             "NAME": applicant_data.applicant_name,
             "PHONE": [{"VALUE": applicant_data.applicant_phone, "VALUE_TYPE": "WORK"}],
             "SOURCE_ID": "WEBFORM",
             "ASSIGNED_BY_ID": 1}}

    push_bitrix(lead_data)


@app.post("/message_customer")
async def register_customer(customer_email=Form(), customer_name=Form(), customer_phone=Form()):
    try:
        customer_data = CustomerData(customer_name=customer_name, customer_phone=customer_phone,
                                     customer_email=customer_email)
    except ValidationError as e:
        # Обработка ошибки валидации
        error_messages = {error['loc'][0]: error['msg'] for error in e.errors()}
        if 'customer_email' in error_messages:
            raise HTTPException(status_code=400, detail="Неверный формат email.")
        logger.error(f"Ошибка валидации данных: {error_messages}")
        raise HTTPException(status_code=400, detail="Ошибка валидации данных.")

    lead_data = {
        "fields": {
            "TITLE": "Новый лид Заказчик",
            "NAME": customer_data.customer_name,
            "PHONE": [{"VALUE": customer_data.customer_phone, "VALUE_TYPE": "WORK"}],
            "EMAIL": [{"VALUE": customer_data.customer_email, "VALUE_TYPE": "WORK"}],
            "SOURCE_ID": "WEBFORM",
            "ASSIGNED_BY_ID": 1
        }
    }

    push_bitrix(lead_data)


def push_bitrix(lead_data):
    user.create_lead(lead_data)
    raise HTTPException(status_code=HTTP_204_NO_CONTENT)
