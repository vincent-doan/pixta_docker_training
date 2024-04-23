FROM python:3.9

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libgl1-mesa-glx \
        libglib2.0-0 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN chmod +x /app/start.sh
RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["./start.sh"]
