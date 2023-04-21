import json
import os

path_in = r'ВХІД'




def json_to_data(input_file:str)->list:
        list_data = []
        with open(input_file,'r') as input_file_data:
            list_coord = json.load(input_file_data)['coordinates'][0][0]
            for i in list_coord:
                list_data.append(f'{list_coord.index(i) + 1001},{i[0]},{i[1]},')
        return list_data

def txt_to_data(input_file:str)->list:
    with open(input_file, 'r') as input_file_data:
        list_data = (input_file_data.read()).strip().split('\n')
        return list_data




