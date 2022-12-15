class Group:
    '''
    Магические методы
    '''

    def __init__(self, number, name):
        self.name = name
        self.number = number
        self._students = []

    def add(self, student):
        '''
        * Добавляем студентов списком *
        :param student: список
        :return: new list
        '''
        for i in student:
            self._students.append(i)

    def __str__(self):
        text =f'''
        {self.number}{self.name} класс.
        {len(self._students)} чел.
        '''
        return text

    def __len__(self):
        '''
        len(Group)
        :return: длину нужного нам списка
        '''
        return len(self._students)

    def __getitem__(self, n):
        '''
        Group[1] берём по индексу...
        :param n: запрашиваем нужный нам индекс
        :return: значение из списка
        '''
        return self._students[n-1]

    def __eq__(self, other):
        '''
        Сравнение классов
        :param other: ==
        :return:
        '''
        return len(self) == len(other)

    def __contains__(self, item):
        '''
        Проверяем есть ли студент в списке
        :param item: Студент...
        :return: Bool
        '''
        return item in self._students


if __name__=='__main__':

    lst1 = ['Jessica', 'Leo', 'Mike', 'Sofi']
    lst2 = ['Maria', 'Nina', 'Jeck']

    class_1A = Group(1, 'A')
    class_1E = Group(1, 'E')

    class_1A.add(lst1)
    class_1E.add(lst2)


    print('есть' if class_1E[1] in class_1A else 'нет')
