FROM python:3.12-slim

COPY fastAPI.py /fastAPI.py
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

CMD ["python","fastAPI.py"]