FROM python:3.9
#copy files to image
WORKDIR /pythonproject
COPY . .
RUN pip install git+https://github.com/Artory/drf-hal-json@master

#install requirments
RUN pip install -r requirements.txt

CMD [ "python","./dashboard.py" ]
