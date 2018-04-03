from __future__ import print_function
import requests
from pprint import pprint

value = 0


def get_by_key(my_json, ser):
    global value
    for key in my_json.keys():
        if isinstance(my_json[key], (str, int, long, unicode)):
            key = key.encode('utf-8')
            if key.strip() == ser.strip():
                value = my_json.get(key)
        elif isinstance(my_json[key], dict):
            get_by_key(my_json[key], ser)
        elif isinstance(my_json[key], list):
            for item in my_json[key]:
                get_by_key(item, ser)
    return value


def get_by_path(my_json, path='error/data/0/message'):
    remain = None
    mykeys = path.split('/')
    for key in mykeys:
        if all(char.isdigit() for char in key):
            my_json = my_json[int(key)]
        else:
            remain = my_json.get(key)
            my_json = remain
    return remain

# Driver Code

def main():
    q = requests.get('https://clients6.google.com/rpc')
    my_json = q.json()
    pprint(my_json)
    print(get_by_path(my_json, 'error/data/0/message'))
    print(get_by_key(my_json, 'domain'))


if __name__ == "__main__":
    main()
