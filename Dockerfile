FROM python:alpine
WORKDIR /app
WORKDIR /app/WOG
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8777
CMD python main_score.py
