import re
from collections import Counter


def load_data(filepath):
    with open(filepath) as file:
        data = re.findall(r'\w+', file.read().lower())
    return data


def get_most_frequent_words(text):
    return Counter(text).most_common(10)


if __name__ == '__main__':
    text = load_data(input('Введите путь до файла: '))
    frequent_words = get_most_frequent_words(text)
    for word, counter in frequent_words:
        print('{0} - {1}'.format(word, counter))
