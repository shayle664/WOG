FROM python:alpine
WORKDIR /app
RUN apk add --no-cache git
RUN git clone https://github.com/shayle664/WOG.git
WORKDIR /app/WOG
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["sh", "-c", "python main_score.py && python e2e.py"]
