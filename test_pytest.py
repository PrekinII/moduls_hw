import pytest

from application.db.people import people
from application.salary import salary


def test_salary():
    assert salary() == 'Вывод данных по зарплатам'


def test_people():
    assert people() == 'Вывод данных о сотрудниках'


if __name__ == '__main__':
    pytest.main()
