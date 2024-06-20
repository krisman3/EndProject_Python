class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname} - {self.age} years old"


class PersonManager:

    def __init__(self, people_list):
        self.people_list = people_list

    def add_person(self, person: Person):
        self.people_list.append(person)

    def remove_person(self, identifier: str):
        for person in self.people_list:
            if person.name == identifier or person.surname == identifier:
                self.people_list.remove(person)
                break  # This will remove only the first match.

    def __str__(self):
        return '\n'.join(str(person) for person in self.people_list)


person1 = Person("Kristiyan", "Iliev", 28)
person2 = Person("Maria", "Eneva", 25)
person3 = Person("Ivan", "Koev", 29)

### Tests for the task ###

"""
people = []
# management = PersonManager(people)
# 
# management.add_person(person1)
# management.add_person(person2)
# management.add_person(person3)
# management.add_person(person2)
# 
# print(management)
# 
# management.remove_person('Koev')
# print()
# print(management)
"""
