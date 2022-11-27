import json

INPUT_FILE = "output1.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as f:
        output = []
        lines = f.read().splitlines()
        column_names = lines[0].split(',')
        for index, line in enumerate(lines):
            d = dict()
            if index == 0:
                continue
            entries = line.split(',')
            for i, column_name in enumerate(column_names):
                d[column_name] = entries[i]
            output.append(d)
    return output


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
