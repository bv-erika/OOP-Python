import calendar
from datetime import date
from multipledispatch import dispatch


class EmployeeThird(object):
    def __init__(self, name, birthDay=date(2000,12,1), salary=150000):
        self.__birthDay = birthDay
        self.__name = name
        self.__salary = salary

    def __str__(self):
        return "Name:" + self.get_name() + "\nSalary:" + str(self.get_salary()) + "\nBirthday:" + str(self.get_birthDay())

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_birthDay(self):
        return self.__birthDay

    def set_birthDay(self, birthDay):
        self.__birthDay = birthDay

    def increaseSalary(self, percentage):
        self.__salary += self.__salary * percentage / 100

    @dispatch(int, int, int)
    def createDay(self, year, month, day):
        return date(year, month, day)

    @dispatch(int, str, int)
    def createDay(self, year, month_name, day):
        month = list(calendar.month_name).index(month_name)
        return date(year, month, day)
