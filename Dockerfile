FROM python:3.10-slim
WORKDIR /app
RUN pip install flask
# This copies the 'app' folder content into /app
COPY app/ . 
# This runs the file directly from the /app folder
CMD ["python", "anamika_service.py"]
