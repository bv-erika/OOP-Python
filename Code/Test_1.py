from Classes.EmployeeFirst import EmployeeFirst

e1 = EmployeeFirst("Deniz", 150000)
e2 = EmployeeFirst("Eren", 121001)
print(e1.__str__())
print(e2.__str__())
e1.increaseSalary(10)
e2.increaseSalary(10)
print(e1.__str__())
print(e2.__str__())
