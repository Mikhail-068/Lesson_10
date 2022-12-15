import pytest
from persons02 import Person


class TestPerson:

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_age_property(self):
        person = Person('Max', 20)
        # assert False
        assert person.age == 20

    def test_init(self):
        person = Person('Max', 20)
        assert person.name == 'Max'
        assert person.age == 20
        # Это не должно работать
        person = Person('Max', -20)


    def test_age_setter_exception(self):
        person = Person('Max', 20)
        # Должна быть ошибка
        try:
            person.age = -40
        except:
            assert True
        else:
            assert False

        # более красивая запись через raises
        # В скобках ошибка которую мы ожидаем получить
        with pytest.raises(ValueError):
            # Поведение которое должно выдать эту ошибку
            person.age = -40

    def test_age_setter_valid(self):
        person = Person('Max', 20)
        person.age = 40
        assert person.age == 40
