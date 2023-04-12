from datetime import datetime, date

from Classes.EmployeeFourth import EmployeeFourth


def main():
    e1 = EmployeeFourth("Deniz",birthDay=date(1999,10,5))
    e2 = EmployeeFourth(name="Eren",salary=12000,emails=["eren@gmail.com","second@gmail.com"])
    print(e1.__str__())
    print(e2.__str__())
    print("-*-*-*-*-*-*-*-*-")
    e1.add_email("first@gmail.com")
    e2.set_birthDay(e2.createDay(1970,"February",22))
    e2.add_email("third@gmail.com")
    print(e1.__str__())
    print(e2.__str__())


if __name__ == "__main__":
    main()
