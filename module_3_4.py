# Цель: закрепить знание использования параметров *args/ **kwargs на практике

# Задача "Однокоренные"

def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    other_words = list(other_words)
    other_words = [s.lower() for s in other_words]
    for i in range(len(other_words)):
        if root_word in other_words[i]:
            same_words.append(other_words[i])
        elif other_words[i] in root_word:
            same_words.append(other_words[i])
        else:
            continue
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)




