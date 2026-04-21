# Лабораторная работа 3: Паттерн Adapter

## Описание
Демонстрация паттерна Adapter на примере мониторинга Redis с помощью Prometheus.

## Структура
- **Redis** - основной контейнер
- **redis_exporter** - контейнер-адаптер для Prometheus

## Файлы
- `manifests/adapter-pod.yaml` - Pod с Redis и адаптером
- `manifests/service.yaml` - Service для доступа к метрикам
- `manifests/service-monitor.yaml` - ServiceMonitor для Prometheus

## Развертывание

### Установка Prometheus Operator
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack
kubectl apply -f manifests/
kubectl port-forward svc/adapter-example 9121:9121
curl localhost:9121

# Запустить Minikube (уже установлен)
minikube start

# Деплой
kubectl apply -f manifests/

# Проверить
kubectl get pods
kubectl port-forward svc/adapter-example 9121:9121
mkdir -p manifests && cd manifests
cat > adapter-pod.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: adapter-example
  namespace: default
  labels:
    app: adapter-example
spec:
  containers:
    - image: redis:latest
      name: redis
    - image: oliver006/redis_exporter:latest
      name: adapter
# Лабораторная 6: Паттерн Decorator

## Код функции

```python
import random
import json

def random_name():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    return random.choice(names)

def handle(req):
    obj = json.loads(req) if req else {}
    
    if not obj.get("name"):
        obj["name"] = random_name()
    if not obj.get("color"):
        obj["color"] = "blue"
    
    return json.dumps(obj)
  # Лабораторная 6: Паттерн Decorator

## Реализация функции-декоратора

```python
import random
import json

def random_name():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    return random.choice(names)

def handle(req):
    obj = json.loads(req) if req else {}
    
    if not obj.get("name"):
        obj["name"] = random_name()
    if not obj.get("color"):
        obj["color"] = "blue"
    
    return json.dumps(obj)