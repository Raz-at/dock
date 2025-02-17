FROM python:3.6
RUN apt-get update
 
COPY . /DOCK
WORKDIR /DOCK


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","postgres.py"]
