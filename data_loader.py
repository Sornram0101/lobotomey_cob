# data_loader.py
import json
import os
from entities import Abnormality

def load_monsters():
    # กำหนด Path ให้ถูกต้องเพื่อป้องกันบั๊กหาไฟล์ไม่เจอ
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'data', 'monsters.json')
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return [Abnormality(m['id'], m['name'], m['risk_level'], m['max_counter']) for m in data['monsters']]