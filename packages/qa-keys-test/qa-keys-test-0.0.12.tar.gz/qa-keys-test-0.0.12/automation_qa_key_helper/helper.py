import os
import json
from types import SimpleNamespace

# config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'qa_key.json')
config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qa_key.json')
def get_qa_key():
    with open(config_file_path, 'r', encoding='utf-8') as f:
        config_data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
        return config_data
