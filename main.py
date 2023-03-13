class FlatIterator:

    def __init__(self,list_of_list):
        """Определяет атрибут для хранения списка списков"""
        self.list_of_list = list_of_list


    def __iter__(self):
        """Определяет атрибуты для итерации по списку"""
        self.list_iter = iter(self.list_of_list)  # определяем итератор для списка
        self.list_of_lists_1 = []  # определяем вложенный список для добавления элементов
        self.cursor = -1  # смещаем курсор за границу списка
        return self

    def __next__(self):
        """Определяет и возвращает следущий элемент списка списков"""
        self.cursor += 1
        if len(self.list_of_lists_1) == self.cursor:  # если курсор в конце вложенного списка, то "обнуляем" список и курсор
            self.list_of_lists_1 = None
            self.cursor = 0
            while not self.list_of_lists_1:  # если вложенные списки закончились, то получаем stop iteration
                self.list_of_lists_1 = next(self.list_iter)  # если  список пустой, то получаем следующий вложенный список
        return self.list_of_lists_1[self.cursor]


def flat_generator(list_of_list):
    """Генератор позволяет  возвращать эелементы из списка списков с двойным уровнем вложености"""
    for sub_list in list_of_list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':
    list_of_lists_1= [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    print('*' * 20)
    print('Вызов итератора')
    for item in FlatIterator(list_of_lists_1):
        print(item)
    print('*' * 20)

    print('_' * 20)
    print('Вызов компрехеншен')
    flat_list = [item for item in FlatIterator(list_of_lists_1)]
    print(flat_list)
    print('_' * 20)

    print('+' * 20)
    print('Вызов генератора')
    for item in flat_generator(list_of_lists_1):
        print(item)
    print('+' * 20)