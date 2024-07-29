FROM python:3.9-slim-buster

WORKDIR /web
COPY . /web
RUN mkdir /etc/cert
RUN python3 -m pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
