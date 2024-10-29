# Домашнее задание по теме "Генераторы"

# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python

def all_variants(text):
    n = len(text)

    for length in range(1, n + 1):
        for start in range(n - length + 1):
            yield text[start:start + length]

for variant in all_variants("12345"):
    print(variant)