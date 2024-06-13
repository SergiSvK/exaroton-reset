FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# =============== TOKEN API ===============

ENV TOKEN=""
ENV HOUR=""
ENV MINUTE=""
ENV TIMEZONE=""
ENV WEEBHOOK=""

CMD ["python", "main.py"]