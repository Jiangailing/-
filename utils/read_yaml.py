import yaml


def get_baseurl(path, baseurl, keyurl):
    #   ��ȡyaml�ļ��ж�Ӧ������url·���������ظ��ӿڽ���urlƴ��

    with open(path, "r", encoding="utf8") as f:
        yaml_url = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_url)
        f.close()
    return yaml_url[baseurl][keyurl]


def read_yaml(path):
    # ��ȡ��ȡtoken�ӿ�����Ĳ��������ӿ����������װ��yaml�ļ��е�ԭ���ǣ��������ά�����޸�
    with open(path, "r", encoding="utf8") as f:
        yaml_ob = yaml.load(f, Loader=yaml.FullLoader)
        print(yaml_ob)
        f.close()
    return yaml_ob

# if __name__ == '__main__':
#     read_yaml("../get_token.yml")
