FROM continuumio/miniconda3:latest

WORKDIR /

COPY . .

EXPOSE 80

CMD ["python", "-m",  "http.server", "80"]