import yaml


def main():
    # 需要写的文件内容
    data = {"Search_Data": {
        "search_test_001": {"except": {"value": "你好"}, "value": "你好"},
        "search_test_002": {"except": [4, 5, 6], "value": 456}
    }}
    with open("./text.yml", "w") as f:
        # 在当前目录下生成text.yaml文件，若文件存在直接更新内容
        yaml.dump(data, f, encoding='GBK', allow_unicode=True)

    # 读取yaml文件
    # with open("./data.yml", "r") as f:
    #     data = yaml.safe_load(f)
    #     # print(type(data)) # 打印data类型
    #     print(data)


if __name__ == "__main__":
    main()

