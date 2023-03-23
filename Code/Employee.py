class Employee:

    def __init__(self, name, salary, birthday, email, position):
        self.emailList = []
        self.name = name
        self.salary = salary
        self.birthday = birthday
        self.emailList.append(email)
        self.position = position

    def setBirthday(self, birthday):
        self.birthday = birthday

    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def getBirthday(self):
        return self.birthday

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary

    def getEmailList(self):
        return self.emailList

    def getPosition(self):
        return self.position

    def increaseBy10(self):
        self.salary = self.salary + self.salary * 10 / 100

    def addEmail(self, email):
        self.emailList.append(email)

    def removeEmail(self, email):
        self.emailList.remove(email)

    def print(self):
        print("Name:", self.getName(), "\nSalary:", self.getSalary(), "\nBirthday: ", self.getBirthday(), "\nPosition: ", self.getPosition(),
              "\nEmails:", self.getEmailList())
