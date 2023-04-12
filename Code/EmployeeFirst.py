class EmployeeFirst(object):
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __str__(self):
        return "Name:" + self.get_name() + "\nSalary:" + str(self.get_salary())

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def increaseSalary(self, percentage):
        self.__salary += self.__salary * percentage / 100
