class Group:
    '''
    Магические методы
    '''

    def __init__(self, number, name):
        self.name = name
        self.number = number
        self._students = []
    def __str__(self):
        text = f'''
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
        return self._students[n - 1]
    def __contains__(self, item):
        '''
        Проверяем есть ли студент в списке
        :param item: Студент...
        :return: Bool
        '''
        return item in self._students
    def __eq__(self, other):
        return len(self) == len(other)
    def __ne__(self, other):
        return len(self) != len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __le__(self, other):
        return len(self) <= len(other)
    def __gt__(self, other):
        return len(self) > len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __add__(self, other):
        new_stud = self._students + other._students
        class_1B = Group(1, 'Б')
        return self._students + other._students


    def add(self, student):
        '''
        * Добавляем студентов списком *
        :param student: список
        :return: new list
        '''
        for i in student:
            self._students.append(i)
    def remove(self, student):
        return self._students.remove(student)
    def show(self):
        print(self._students)


if __name__ == '__main__':
    lst1 = ['Jessica', 'Leo', 'Mike', 'Sofi']
    lst2 = ['Maria', 'Nina', 'Jack']

    class_1A = Group(1, 'A')
    class_1E = Group(1, 'E')

    class_1A.add(lst1)
    class_1E.add(lst2)

    print(len(class_1E), len(class_1A))
    class_1A += class_1E
    print(class_1A)

