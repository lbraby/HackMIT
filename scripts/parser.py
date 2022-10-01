import json

def import_data(path: str):
    with open(path, "r") as fd:
       result = json.loads(fd) 
       print(result)
    return result

def main():
    print(import_data("../data/dawn-event.json"))

