class Person:

    def a(self, val):
        print(f'a c параметром {val}')

    def a(self):
        print('a без параметров')

    def __init__(self, name, age):
        self.name = name
        # Инкапсуляция 1 вид
        self._age = age
        # Инкапсуляция 2 вид
        # self.__age = age

    @property
    def age(self):
        """
        Метод доступа на чтение
        :return: age
        """
        # print('Этот метод был вызван когда написанил obj.age')
        return self._age

    @age.setter
    def age(self, new_age):
        """
        Метод для записи возраста
        :param new_age:
        :return:
        """
        if new_age < 0:
            raise ValueError('Возраст не может быть отрицательными')
        self._age = new_age


class B:
    def __private(self):
        print("Это приватный метод!")

    def _private(self):
        print("Это приватный метод!")


if __name__ == '__main__':
    max = Person('Max', 20)

    print(max.age)

    max.age = 10

    print(max.age)

    # Возраст не может быть отрицательным, будет Exception
    # max.age = -10

    print(max.age)

    max.a()