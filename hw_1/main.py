from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    print(f'{datetime.date(datetime.now())}')
    print(f'{get_employees()}')
    print(f'{calculate_salary()}')