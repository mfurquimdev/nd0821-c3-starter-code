FROM ubuntu:22.04 AS builder

RUN apt update

RUN apt-get install -y inotify-tools

FROM python:latest

COPY --from=builder /usr/bin/inotifywait /usr/bin/inotifywait

# Set the working directory
WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the script to the folder
COPY . /app

# Start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
