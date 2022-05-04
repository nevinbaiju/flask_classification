FROM python:3

COPY . /home/app/
WORKDIR /home/app

RUN pip install -r requirements.txt
RUN python create_model.py

EXPOSE 81

CMD ["python", "app.py"]