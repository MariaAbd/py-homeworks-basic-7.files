from pprint import pprint
import os
path = os.getcwd()


sorted_texts = []
text_dict = {}


def get_data(path):
    for file_name in os.listdir(path):
        if file_name.endswith(".txt"):
            with open(file_name, encoding='utf-8') as file:
                text_size = len(file.readlines())
            sorted_texts.append([text_size, file_name])
            sorted_texts.sort()


def write_files(path):
    for file_name in os.listdir(path):
        if file_name.endswith(".txt"):
            with open(file_name, encoding='utf-8') as file:
                text_dict[file_name] = ''.join(file.readlines())


def write_data(file_name):
    with open(file_name, mode='w', encoding='utf-8') as file:
        for text in sorted_texts:
            file.write(str(text[1]) + '\n')
            file.write(str(text[0]) + '\n')
            file.writelines(str(text_dict[text[1]]))
            file.write('\n')


def read_data(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        for line in file:
            pprint(str(line))


get_data(path)
write_files(path)
write_data('finish.docx')
read_data('finish.docx')

