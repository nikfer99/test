# Лабораторные работы по паттернам контейнеризации

## Лабораторная 3: Паттерн Adapter
- Redis + redis_exporter
- Адаптер преобразует метрики Redis в формат Prometheus

## Лабораторная 4: Реплицированные сервисы
- Тестовый сервер (3 реплики)
- Балансировка нагрузки через Service

## Лабораторная 5: Sharded Memcached + Ambassador
- StatefulSet с 3 шардами Memcached
- Twemproxy как Ambassador
- Проверка: set/get test → STORED / hello

## Лабораторная 6: Паттерн Decorator

### Код функции

` ` `python
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
` ` `

### Результаты

| Вход | Выход |
|------|-------|
| `{}` | `{"name": "Alice", "color": "blue"}` |
| `{"name": "John"}` | `{"name": "John", "color": "blue"}` |
| `{"color": "red"}` | `{"name": "Bob", "color": "red"}` |

## Ссылка
https://github.com/nikfer99/test
