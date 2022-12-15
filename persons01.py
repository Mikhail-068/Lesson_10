class Person:

    def __init__(self, name, age):
        self.name = name
        # Инкапсуляция 1 вид
        self._age = age
        # Инкапсуляция 2 вид
        # self.__age = age

    def get_age(self):
        """
        Метод доступа на чтение
        :return: age
        """
        return self._age

    def set_age(self, new_age):
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

    print(max.get_age())

    max.set_age(10)

    print(max.get_age())

    # Возраст не может быть отрицательным, будет Exception
    # max.set_age(-10)

    print(max.get_age())

    # max.__age = 100

    # print(max.__age)

    # b = B()
    # # b.__private()
    #
    # b._private()
    # b._B__private()
