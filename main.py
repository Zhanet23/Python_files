import os
import sys
import uuid

def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(source: str, dest: str, num_row: int):
    """
    Функция для переноса указанной строки из одного файла в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """
     
    with open(source, "r", encoding="utf-8") as file:  # ищем информацию по номеру введенной строки, результат будет в res
        res = ""
        for ind, line in enumerate(file):
            if ind == num_row:
                res = line
        if len(res) == 0:
            print(f'Строки с таким номером {num_row} нет в исходном файле.')
            return
        
    if dest == "":
        print("Вы не ввели имя файла, куда копировать выбранную информацию. Информация будет сохранена во временном файле")
        dest = str(uuid.uuid4())
        flag = "w"
    elif dest not in os.listdir() and dest != "":
        print(f'указанное имя файла отсутствует. Файл {dest} будет создан')
        flag = "w"
    else:
        otvet = (input("Вы хотите добавить информацию (1) к старой или перезаписать (enter)? "))
        if otvet != "" and int(otvet) == 1:
            flag = "a"
        else:
            flag = "w"

    with open(dest, flag, encoding="utf-8") as file_1:
        file_1.write(res)  
    print(f'копируемая информация: {res} сохранена в файле {dest}.')  
        

INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
"""

file = "Text.txt"

if file not in os.listdir():
    print("указанное имя файла отсутсвует")
    sys.exit()
 
while True:
    mode = int(input(INFO_STRING))
    match mode:
        case 1:
            print(read_all(file))
        case 2:
            name = input("Введите Ваше имя: ")
            phone = input("Введите Ваш телефон: ")
            add_new_user(name, phone, file)
        case 3:
            data = input("Введите значение: ")
            print(search_user(file, data))
        case 4:
            dest = input("Введите название файла, куда хотите скопировать информацию: ")
            num_row = (input("Введите № строки, информацию с которой хотите скопировать (нумерация начинается с 0): "))
            if num_row == "":
                print("Номер строки не корректный")
            elif int(num_row) < 0:
                print("Номер строки не может быть отрицательный")
            else:
                transfer_data(file, dest, int(num_row))











        