import yaml


with open('b_yaml_test.yaml') as f:
    film = yaml.load(f, Loader=yaml.FullLoader)
    print(film)