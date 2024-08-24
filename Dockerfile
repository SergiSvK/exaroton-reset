FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# =============== TOKEN API ===============

ENV TOKEN=""
ENV TIMEZONE=""
ENV WEBHOOK_URL=""
ENV CRON_SCHEDULE=""
ENV ID_SERVER=""
ENV LANGUAGE=""

CMD ["python", "main.py"]