FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
RUN apk add --no-cache chromium
RUN apk add --no-cache chromedriver
RUN git clone https://github.com/shayle664/WOG.git
WORKDIR /app/WOG
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV FLASK_ENV=development
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
