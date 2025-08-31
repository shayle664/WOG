FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
COPY app/ ./app/
RUN pip install -r app/requirements.txt
EXPOSE 5000
CMD ["python", "app/main_score.py"]