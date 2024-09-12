# Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта.
# Написать усовершенствованную функцию записи.

# Задача "Записать и запомнить"

def custom_write(file_name, strings):
    cnt = 0                              # счетчик строк
    cnt_1 = 0                            # переменная для записи байта начала строки
    strings_positions = {}
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        cnt_1 = file.tell()
        file.write(f'{i}\n')
        cnt += 1
        strings_positions[(cnt, cnt_1)] = i
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)




