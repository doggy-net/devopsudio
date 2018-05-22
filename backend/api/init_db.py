from models import enum_manager

import json


def init_db(field_object, json_file_path):
    try:
        with open(json_file_path) as json_file:
            json_content = json_file.read()
            docs = json.loads(json_content)
            for doc in docs:
                field_object(**doc).save()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    init_db(enum_manager.Enum, 'db_data\\Enum.json')
