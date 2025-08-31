FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
RUN git clone https://github.com/shayle664/WOG.git .
RUN pip install -r app/requirements.txt
EXPOSE 5000
CMD ["python", "app/main_score.py"]