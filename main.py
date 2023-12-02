from application.db.people import people
from application.salary import salary
from datetime import datetime


if __name__ == '__main__':
    print(people())
    print(salary())
    print(datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S'))
