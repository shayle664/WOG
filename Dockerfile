FROM python:alpine
WORKDIR /app/WOG
RUN apk add --no-cache git chromium chromium-chromedriver \
    && pip install flask==2.0.3 werkzeug==2.0.3 selenium==4.0.0
EXPOSE 8777
ENV DISPLAY=:99
CMD python main_score.py
