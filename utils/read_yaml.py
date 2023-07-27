# -*- coding: gbk -*-
import yaml


def get_baseurl(path, baseurl, keyurl):

    with open(path, "r", encoding="utf8") as f:
        yaml_url = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_url)
        f.close()
    return yaml_url[baseurl][keyurl]


def read_yaml(path):

    with open(path, "r", encoding="utf8") as f:
        yaml_ob = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_ob)
        f.close()
    return yaml_ob

# if __name__ == '__main__':
#     read_yaml("../get_token.yml")
