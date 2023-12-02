import pytest

from application.db.people import get_employees
from application.salary import calculate_salary


def test_salary():
    assert calculate_salary() == 'Вывод данных по зарплатам'


def test_people():
    assert get_employees() == 'Вывод данных о сотрудниках'


if __name__ == '__main__':
    pytest.main()
