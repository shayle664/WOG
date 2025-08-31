FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
COPY app/ ./
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main_score.py"]