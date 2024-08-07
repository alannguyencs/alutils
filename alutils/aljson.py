import json


def load(json_path):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def save(json_data, json_path):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False)