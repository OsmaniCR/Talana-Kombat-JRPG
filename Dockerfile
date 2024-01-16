FROM python:3.12-slim
LABEL authors="OsmaniCR"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8008

CMD ["uvicorn", "run:app", "--host=0.0.0.0", "--port=8008",  "--reload"]

