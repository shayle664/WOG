FROM python:alpine
WORKDIR /app/WOG
RUN apk add --no-cache git chromium chromium-chromedriver
RUN git clone https://github.com/shayle664/WOG.git .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8777
CMD python main_score.py
