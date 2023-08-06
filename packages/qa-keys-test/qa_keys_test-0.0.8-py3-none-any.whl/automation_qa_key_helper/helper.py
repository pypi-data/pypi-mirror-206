import os
import json

# config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'qa_key.json')
config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'qa_key.json')
def get_qa_key():
    with open(config_file_path, 'r', encoding='utf-8') as f:
        config_data = json.load(f)
        # print(config_data)
        return config_data
