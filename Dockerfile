FROM python:3.8-buster
WORKDIR /app
COPY Calculator_main.py .
COPY requirements.txt .
COPY Scientific_Calculator.py .
RUN pip3 install -r requirements.txt

#File will be run from here onwards
ENTRYPOINT python3 Calculator_main.py
