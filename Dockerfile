FROM python:3.10
WORKDIR /code
ADD . /code
# Install the ping command
RUN apt-get update && apt-get install -y vim
RUN pip3 install -r requirements.txt
COPY . /code
CMD ["python3", "main.py"]
