import json

def read_json(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = json.load(file)
        return content


def iterate_list(iterable_sequence):
    try:
        yield from iterable_sequence
    except Exception:
        print('Должен быть список')
        raise


if __name__ == "__main__":
    FILE_NAME = 'flowers.json'
    list_of_flowers = read_json(file_name=FILE_NAME)
    flowers = iterate_list(list_of_flowers)
    print(flowers)

