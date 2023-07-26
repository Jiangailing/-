import yaml


def get_baseurl(path, baseurl, keyurl):
    #   读取yaml文件中对应环境的url路径，并返回给接口进行url拼接

    with open(path, "r", encoding="utf8") as f:
        yaml_url = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_url)
        f.close()
    return yaml_url[baseurl][keyurl]


def read_yaml(path):
    # 读取获取token接口请求的参数，将接口请求参数封装到yaml文件中的原因是：方便后期维护和修改
    with open(path, "r", encoding="utf8") as f:
        yaml_ob = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_ob)
        f.close()
    return yaml_ob

# if __name__ == '__main__':
#     read_yaml("../get_token.yml")
