# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

COPY Scores.txt /Scores.txt

CMD ["python", "main_score.py"]
