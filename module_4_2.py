# Домашнее задание по уроку "Пространство имен"

def test_function():
    def inner_function():
        print('Я в области видимости test_function')

    inner_function()

test_function()

inner_function() # данная функция не может быть вызвана вне функции test_function