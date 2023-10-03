# Sentiment Analysis Web App with Prometheus Monitoring

This project is a web application that performs sentiment analysis using a BERT model. It includes a complete infrastructure with monitoring using Prometheus and Grafana.

## Architecture

The project's architecture consists of the following components:

- **Nginx Web Server**: A custom image that serves the front-end of the application on port 80.

- **Nginx Prometheus Exporter**: Exposes Nginx metrics for Prometheus on port 9113.

- **Flask Backend**: Hosts the sentiment analysis API on port 8000. It contains a BERT model that evaluates sentiment as positive/negative.

- **MongoDB**: A database for storing user input and sentiment analysis results on port 27017.

- **MongoDB Exporter**: Exposes MongoDB metrics for Prometheus on port 9216.

- **Prometheus**: Collects and stores metrics from various components on port 9090.

- **Grafana**: Provides a dashboard for visualizing and monitoring Prometheus metrics on port 3000.


## Expected result
Deploy with docker compose
```
$ docker compose up -d
```

Listing containers must show eight containers running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS         PORTS                      NAMES
586ee4d473a8   01docker-compose-bert-web         "/docker-entrypoint.…"   7 minutes ago   Up 7 minutes   0.0.0.0:80->80/tcp         01docker-compose-bert-web-1
62de04a6bc10   grafana/grafana                   "/run.sh"                7 minutes ago   Up 7 minutes   0.0.0.0:3000->3000/tcp     01docker-compose-bert-grafana-1
5ae1153c29a7   01docker-compose-bert-backend     "flask run"              7 minutes ago   Up 7 minutes   8000/tcp                   01docker-compose-bert-backend-1
7280d6a23e5e   prom/prometheus                   "/bin/prometheus --c…"   7 minutes ago   Up 7 minutes   0.0.0.0:9090->9090/tcp     01docker-compose-bert-prometheus-1
66a237f85189   bitnami/mongodb-exporter          "mongodb_exporter"       7 minutes ago   Up 7 minutes   0.0.0.0:9216->9216/tcp     01docker-compose-bert-mongodb-exporter-1
a2bafff7f34a   prom/node-exporter                "/bin/node_exporter"     7 minutes ago   Up 7 minutes   0.0.0.0:9100->9100/tcp     01docker-compose-bert-node-exporter-1
f574b2dca173   nginx/nginx-prometheus-exporter   "/usr/bin/nginx-prom…"   7 minutes ago   Up 7 minutes   0.0.0.0:9113->9113/tcp     01docker-compose-bert-nginx-exporter-1
fea7b6b050ad   mongo:latest                      "docker-entrypoint.s…"   7 minutes ago   Up 7 minutes   0.0.0.0:27017->27017/tcp   01docker-compose-bert-db-1
```

After the application starts, navigate to `http://localhost:80` in your web browser for the sentiment analysis, `http://localhost:9090` for Prometheus and `http://localhost:3000` for Grafana

Stop and remove the containers
```
$ docker compose down
```
