import yaml

# f = open('d1.yaml', encoding='utf-8')

with open('../config/d1.yaml', encoding='utf-8') as f:
    data = yaml.load(f.read(), Loader=yaml.FullLoader)
print(data)
