import os
import pandas as pd

def getfiles(dir = os.getcwd()):
    filelist = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            if filename.count('.php') or filename.count('.js'):
                filelist.append(os.path.join(dirpath, filename))
    return filelist

def parcer():
    way_to_file = input(str('Введите путь до файла(если путь окажется некорректным программа вернёт пустой файл): \n'))
    if way_to_file == '':
        mass = getfiles()
    else:
        mass = getfiles(way_to_file)
    output = []
    for i in mass:
        cheq = ''

        with open(i, "r", encoding="latin-1") as file:
            cheq = file.read()

        if cheq.count('/* --------------------- */\n'
                '/* Documented in Wiki.js */\n'
                '/* --------------------- */\n') == 0:
            output.append(i)
    return output

data = parcer()
while True:
    save_as = input(str("Сохранить как:\n"
                        "1. excel фaйл\n"
                        "2. .txt файл\n"))
    if save_as == '1':
        df = pd.DataFrame(data=data)
        df.to_excel('./result.xlsx')
        break
    elif save_as == '2':
        with open('result.txt', 'w') as file:
            for i in data:
                file.write(i + '\n')
        break
    else:
        print("Введите 1 или 2")