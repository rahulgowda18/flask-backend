FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
# This Dockerfile sets up a Python 3.9 environment, installs dependencies from requirements.txt,
# copies the application code into the container, exposes port 5000, and runs app.py