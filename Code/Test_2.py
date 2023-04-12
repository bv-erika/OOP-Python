from Classes.EmployeeSecond import EmployeeSecond

e1 = EmployeeSecond("Deniz")
e2 = EmployeeSecond("Eren",121001)
print(e1.__str__())
print(e2.__str__())
e1.increaseSalary(10)
e2.increaseSalary(10)
print(e1.__str__())
print(e2.__str__())
