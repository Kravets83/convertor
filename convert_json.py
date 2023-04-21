import json
import os

path_in = r'ВХІД'

for file in os.listdir(path_in):
    if file.endswith(".json"):
        file_path = f"{path_in}\\{file}"
        with open(file_path) as input_file:
            a = json.load(input_file)['coordinates'][0][0]
            for i in a:
                print(f'{a.index(i)+1001},{i[0]},{i[1]}')


