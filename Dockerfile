FROM python:3.9-slim

WORKDIR /app

COPY list_app.py signup_app.py db.json ./

RUN pip install flask

EXPOSE 5000 5002

CMD ["sh", "-c", "python signup_app.py & python list_app.py"]
