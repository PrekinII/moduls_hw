from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


if __name__ == '__main__':
    print(get_employees())
    print(calculate_salary())
    print(datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S'))
