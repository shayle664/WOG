FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
RUN git clone https://github.com/shayle664/WOG.git .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install seleniumbase
RUN pip3 install seleniumbase
EXPOSE 8777
CMD python main_score.py