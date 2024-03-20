class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name
    
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print('Age value must be positive!')

person = Person('Person Name', 10)

# Get name
print('Name:', person.get_name())

# Set new name
person.set_name('New Name')
print('Name:', person.get_name())

# Get age
print('Age:', person.get_age())

# Set new age
person.set_age(-5)
print('Age:', person.get_age())


