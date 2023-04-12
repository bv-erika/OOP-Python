import calendar
from datetime import date
from multipledispatch import dispatch


class EmployeeFourth(object):
    def __init__(self, name, birthDay=date(2000, 12, 1), salary=150000, emails=None):
        if emails is None:
            emails = []
        self.__birthDay = birthDay
        self.__name = name
        self.__salary = salary
        self.__emailList = emails

    def __str__(self):
        return "Name:" + self.get_name() + \
            "\nSalary:" + str(self.get_salary()) + \
            "\nBirthday:" + str(self.get_birthDay()) + \
            "\nEmails:" + str(self.get_emails())

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

    def get_emails(self):
        return self.__emailList

    def set_emails(self, emailList):
        self.__emailList = emailList

    def add_email(self, email):
        self.__emailList.append(email)

    def increaseSalary(self, percentage):
        self.__salary += self.__salary * percentage / 100

    @dispatch(int, int, int)
    def createDay(self, year, month, day):
        return date(year, month, day)

    @dispatch(int, str, int)
    def createDay(self, year, month_name, day):
        month = list(calendar.month_name).index(month_name)
        return date(year, month, day)
