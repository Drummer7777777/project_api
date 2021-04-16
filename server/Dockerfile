FROM python:3.7-alpine
WORKDIR /server
COPY requirements.txt /server
RUN pip install -r requirements.txt --no-cache-dir
ADD users.py /server
ADD data_base.json /server
ENTRYPOINT [ "python" ]
CMD ["users.py"]