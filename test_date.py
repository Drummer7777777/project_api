import json
with open('data_base.json', encoding='utf-8') as f:
    users=json.load(f)
    print(users)