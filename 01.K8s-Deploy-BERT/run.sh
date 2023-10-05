#!/bin/bash

kubectl apply -f "cluster-role.yaml"
kubectl apply -f "pvc.yaml"
kubectl apply -f "config-map.yaml"
kubectl apply -f "mongodb.yaml"
kubectl apply -f "flask-app.yaml"
kubectl apply -f "nginx.yaml"
