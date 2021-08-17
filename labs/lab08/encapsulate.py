import datetime

class Student:
    # To abide by pytest needs. Includes a getAge and getName functionality 
    def __init__(self, firstName, lastName, birth_year):
        self.name = firstName + " " + lastName
        self.birth_year = birth_year
    
    # Makes the age calculation less rigid
    # Gets the time right now, rather than just 2019
    def getAge(self):
        return datetime.datetime.now().year - self.birth_year

    def getName(self):
        return self.name

if __name__ == '__main__':
    s = Student("Rob", "Everest", 1961)
    years_old = s.getAge
    print(f"{s.name} is {years_old} old")
