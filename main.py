import json
import os
import time as ti

import pyautogui as pg
import pyperclip

path_in = r'ВХІД'
path_out = r'ВИХІД'


def open_prog():
    input_prog = r".\coord\Coord.lnk"
    os.startfile(input_prog)
    ti.sleep(1)
    pg.hotkey('Tab')
    pg.press('enter')
    ti.sleep(1)


def enter_x_y():
    
    open_prog()
    for file in os.listdir(path_in):
        name = f"{path_out}\\{file[:-4] + 'NEW.txt'}"
        input_file = f"{path_in}\\{file}"
        if file.endswith(".txt"):
            list_data = txt_to_data(input_file=input_file)
            write_file(list_data=list_data, file_name=name)
        elif file.endswith(".json"):
            list_data = json_to_data(input_file=input_file)
            write_file(list_data=list_data, file_name=name)
    pg.hotkey('alt', 'f4')
    os.startfile(".\ВИХІД")


def json_to_data(input_file: str) -> list:
    list_data = []
    with open(input_file, 'r') as input_file_data:
        list_coord = json.load(input_file_data)['coordinates'][0][0]
        for i in list_coord:
            list_data.append(f'{list_coord.index(i) + 1001},{i[1]},{i[0]},')
    return list_data


def txt_to_data(input_file: str) -> list:
    with open(input_file, 'r') as input_file_data:
        list_data = (input_file_data.read()).strip().split('\n')
        return list_data


def write_file(list_data: list, file_name: str):
    with open(file_name, 'w') as write_file:
        new_piket = convertor_out_prog(list_data)
        write_file.write("".join(new_piket))


def convertor_out_prog(data: list, ) -> list:
    new_coord_list = []
    for i in data:
        piket = (i.split(','))
        if len(piket) < 3:
            continue
        else:
            pg.doubleClick(200, 195)
            pg.write(piket[1])
            pg.doubleClick(200, 210)
            pg.write(piket[2])
            pg.doubleClick(500, 195)
            pg.hotkey('ctrl', 'c')
            x_coord = pyperclip.paste()
            pg.doubleClick(500, 210)
            pg.hotkey('ctrl', 'c')
            y_coord = pyperclip.paste()
            new_coord_list.append(f'{piket[0]},{x_coord},{y_coord},{piket[3]}\n')

    return new_coord_list


if __name__ == "__main__":
    enter_x_y()
