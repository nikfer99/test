import random
import json

def random_name():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    return random.choice(names)

def handle(req):
    try:
        obj = json.loads(req) if req else {}
    except:
        obj = {}
    
    if obj.get("name") is None:
        obj["name"] = random_name()
    
    if obj.get("color") is None:
        obj["color"] = "blue"
    
    return json.dumps({"result": obj})
