FROM python:3.9-alpine
ADD . /home/app
WORKDIR /home/app
RUN pip install requests
EXPOSE 8080
ENV PYTHONUNBUFFERED=1
CMD ["python", "handler.py"]
