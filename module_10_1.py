# Домашнее задание по теме "Введение в потоки"

# Цель: понять как работают потоки на практике, решив задачу

# Задача "Потоковая запись в файлы"


import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            time.sleep(0.1)
            file.write(f'Какое-то слово № {i}\n')
    return print(f'Завершилась запись в файл {file_name}')

# вызов функции и измерение времени ее работы без использования потоков
start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end = time.time()
print(end - start)

# вызов функции и измерение времени ее работы с использованием потоков
start1 = time.time()

threads = []
for filename, count in zip(['example5.txt', 'example6.txt', 'example7.txt', 'example8.txt'], [10, 30, 200, 100]):
    thread = threading.Thread(target=write_words, args=(count, filename))
    threads.append(thread)
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end1 = time.time()
print(end1 - start1)




