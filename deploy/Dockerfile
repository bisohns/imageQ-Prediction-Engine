FROM python:3.6.5
LABEL maintainer="Domnan Diretnan"
LABEL email="domnandiretnan@gmail.com"
ADD . /app
WORKDIR /app
EXPOSE 8008
RUN pip install -r requirements.txt
#export an environmental variable called PORT
CMD [ "gunicorn", "-b", "8008:8008", "flask_api:app" ]
# access application on localhost:8008