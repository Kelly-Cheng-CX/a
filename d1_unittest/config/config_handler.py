import yaml


def read_yaml(file, encoding='utf-8'):
    with open(file, encoding=encoding) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)


def write_yaml(file, data, encoding='utf-8'):
    with open(file, encoding=encoding, mode='w') as f:
        # 中文处理

        return yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    # 先读取 yaml 数据
    data = read_yaml('d1.yaml')
    # 写入
    write_yaml('python01.yaml',data)
    print(data)
