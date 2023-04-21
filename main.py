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
        if file.endswith(".txt"):
            file_path = f"{path_in}\\{file}"
            with open(file_path, 'r') as input_file:
                data = (input_file.read()).strip().split('\n')
                name = f"{path_out}\\{file[:-4] + 'NEW.txt'}"
                with open(name, 'w') as bbb:
                    bbb.write('')
                for i in data:
                    print(i)
                    piket = (i.strip().split(','))
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
                        new_piket = (f'{piket[0]},{x_coord},{y_coord},{piket[3]}\n')

                        with open(name, 'a') as write_file:
                            write_file.write(new_piket)
    pg.hotkey('alt', 'f4')
    os.startfile("C:\prog\ВИХІД")


if __name__ == "__main__":
    enter_x_y()
