#!/bin/bash

kubectl delete -f "mariadb.yaml"
kubectl delete -f "flask-app.yaml"
kubectl delete -f "apache.yaml"
kubectl delete -f "config-map.yaml"
kubectl delete -f "pvc.yaml"
kubectl delete -f "cluster-role.yaml"
kubectl delete -f "prom-deployment.yaml"
kubectl delete -f "mariadb-secret.yaml"
