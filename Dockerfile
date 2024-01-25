FROM python:3.9.18-slim 

RUN apt-get update -y && apt-get install ffmpeg -y 
WORKDIR /app 
COPY requirements.txt . 
RUN pip install -r requirements.txt 
COPY app . 
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=5000"]