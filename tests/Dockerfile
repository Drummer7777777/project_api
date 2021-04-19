FROM python:3.7-alpine
WORKDIR /client
COPY requirements.txt /client
RUN pip install -r requirements.txt --no-cache-dir
ADD test_example.py /client
ADD data_base.json /client
ADD conftest.py /client
ENTRYPOINT [ "pytest" ]
CMD ["test_example.py"]
