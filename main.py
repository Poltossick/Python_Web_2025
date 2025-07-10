# ООП - (polymorphism)

from lib import Student, Employee, Person

people = [
    Person('Alex'),
    Student('','ITMO'),
    Student('','SPBU'),
    Employee(),
]

for  person in people:
    if isinstance(person, Student):
        print(person.get_university())
    elif isinstance(person, Employee):
        print(person.get_company())
    else:
        print(person.get_name())

