import json

def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = json.load(file)
        return content


if __name__ == "__main__":
    FILE_NAME = 'flowers.json'
    result = read_json(file_name=FILE_NAME)
    print (result)
    
