#!/bin/bash

kubectl apply -f "cluster-role.yaml"
kubectl apply -f "pvc.yaml"
kubectl apply -f "config-map.yaml"
kubectl apply -f "mariadb-secret.yaml"
kubectl apply -f "mariadb.yaml"
kubectl apply -f "flask-app.yaml"
kubectl apply -f "apache.yaml"
kubectl apply -f "prom-deployment.yaml"
