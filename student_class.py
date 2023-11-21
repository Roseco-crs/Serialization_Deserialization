class Student:

    def __init__(self, firstname, surname, id):
        self.firstname = firstname
        self.surname = surname
        self.id = id

    def display(self):
        print(f"Firstname: {self.firstname}, Surname: {self.surname}, ID: {self.id}")
