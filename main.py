class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname} - {self.age} years old"


class PersonManager:

    def __init__(self, people_list):
        self.people_list = list(people_list)

    def add_person(self, person: Person):
        self.people_list.append(person)

    def remove_person(self, identifier: str):
        for person in self.people_list:
            if person.name == identifier or person.surname == identifier:
                self.people_list.remove(person)
                break  # This will remove only the first match.

    def __str__(self):
        for person in self.people_list:
            yield person
    # TO continue implementation on how to print the list


person1 = Person("Kristiyan", "Iliev", 28)

print(person1)
