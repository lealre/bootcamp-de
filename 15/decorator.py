class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print('Age value must be positive!')

person = Person('Person Name', 10)

# Get name
print('Name:', person.name)

# Set new name
person.name = 'New Name'
print('Name:', person.name)

# Get age
print('Age:', person.age)

# Set new age
person.age = -5
print('Age:', person.age)


