FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git chromium chromium-chromedriver
RUN git clone https://github.com/shayle664/WOG.git .
COPY requirements.txt .
RUN pip install flask==2.0.3 werkzeug==2.0.3 selenium==4.0.0
EXPOSE 8777
ENV DISPLAY=:99
CMD python main_score.py
