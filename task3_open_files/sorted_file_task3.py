from pprint import pprint

sorted_texts = []
text_dict = {}


def get_data(file_name):
    with open(file_name, encoding='utf-8') as file:
        lines = 0
        for line in file:
            lines += 1
        sorted_texts.append([lines, file_name])


def write_files(file_name):
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


def sort_data():
    sorted_texts.sort()


get_data('1.txt')
get_data('2.txt')
get_data('3.txt')


sort_data()

write_files('1.txt')
write_files('2.txt')
write_files('3.txt')

write_data('4_sorted.txt')
read_data('4_sorted.txt')



