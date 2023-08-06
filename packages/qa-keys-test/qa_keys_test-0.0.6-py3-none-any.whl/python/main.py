import os
import json

config_file_path = os.path.join('..\config', 'qa_key.json')

with open(config_file_path, 'r', encoding='utf-8') as f:
    config_data = json.load(f)
    print(config_data)
