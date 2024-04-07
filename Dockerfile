FROM python:3.10
COPY . /apps
WORKDIR /apps
RUN python3 -m pip install -r requirements.txt
CMD ["python3", "app.py"]