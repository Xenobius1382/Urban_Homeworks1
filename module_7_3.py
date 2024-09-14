# Домашнее задание по теме "оператор with"

# Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП

# Задача "Найдёт везде"


class WordsFinder():

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower().replace(',', '').replace('.', '').replace('='
                    , '').replace('!', '').replace('?', '').replace(';'
                    , '').replace(':', '').replace(' - ', '')
                    words += line.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        words_dict = self.get_all_words()
        results = {}
        word = word.lower()
        for filename, words in words_dict.items():
            index = words.index(word)
            results[filename] = index + 1  # Для удобства, первый индекс начинаем с 1

        return results

    def count(self, word):
        words_dict = self.get_all_words()
        results = {}
        word = word.lower()
        for filename, words in words_dict.items():
            count = words.count(word)
            results[filename] = count
        return results


finder2 = WordsFinder('test_file.txt', 'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('for'))
print(finder2.count('FoR'))













