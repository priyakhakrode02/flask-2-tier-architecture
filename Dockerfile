FROM python:3.12.1-slim
WORKDIR /my-app
RUN apt-get update -y && apt-get upgrade -y 
COPY requirements.txt .
RUN  pip install -r requirements.txt
RUN  pip install cryptography
COPY . .
CMD ["python", "login_app.py" ]

