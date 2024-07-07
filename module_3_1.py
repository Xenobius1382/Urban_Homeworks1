# Применение на практике начальных знаний о пространстве имён и оператор global. Закрепление навыков из предыдущих модулей.

calls = 0
def count_calls():  # при вызове функции переменная calls увеличивается на еденицу
    global calls
    calls += 1

def string_info(word):   # функция возвращает длинну принимаемого слова, а также переводит его в верхний и нижний регистр
    count_calls()
    tuple = (len(word), word.upper(), word.lower())
    return tuple

def is_contains(word, list_to_search):   # функция принимает слово и список и проверяет, есть ли введенное слово в списке
    count_calls()
    list_to_search = [s.lower() for s in list_to_search]
    word = word.lower()
    if word in list_to_search:
        return True
    else:
        return False

print(string_info('Table'))
print(string_info('Apple'))
print(is_contains('House', ['Han', 'Mouse']))
print(is_contains('Urban', ['Ban', 'Urban']))
print(calls)
