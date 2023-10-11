#!/bin/bash

kubectl delete -f "mongodb.yaml"
kubectl delete -f "flask-app.yaml"
kubectl delete -f "nginx.yaml"
kubectl delete -f "config-map.yaml"
kubectl delete -f "pvc.yaml"
kubectl delete -f "cluster-role.yaml"
kubectl delete -f "prometheus-deployment.yaml"
