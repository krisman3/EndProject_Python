class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class PersonManager:

    def __init__(self, people_list):
        self.people_list = list(people_list)

    def add_person(self, people_list):
        pass

    def remove_person(self, people_list):
    # Must be able to remove a person by name or surname
        pass

    def __str__(self):
        for person in self.people_list:
            print()
    # TO continue implementation on how to print the list