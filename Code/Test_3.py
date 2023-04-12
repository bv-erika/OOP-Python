from Classes.EmployeeThird import EmployeeThird


def main():
    e1 = EmployeeThird("Deniz")
    e2 = EmployeeThird(name="Eren",salary=12000)
    print(e1.__str__())
    print(e2.__str__())
    print("-*-*-*-*-*-*-*-*-")
    e1.set_birthDay(e1.createDay(1999,10,5))
    e2.set_birthDay(e2.createDay(1970,"February",22))
    print(e1.__str__())
    print(e2.__str__())


if __name__ == "__main__":
    main()
