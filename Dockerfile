FROM gcc:latest
FROM python:latest
WORKDIR /main
COPY . /main
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN g++ -o main main.cpp
EXPOSE 80
CMD ["python3", "app.py"]
