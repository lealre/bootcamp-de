# Day 13 - Inheritance and Polymorphism (OOP)

The objective is to create a script that verifies if a new file with a specific format was added in the data folder. To do that, the module `schedule` is used to search in data folder every 5 seconds.

The class `AbstractDataSource` serves as a "base model class," where all other classes that inherit from it must have the same methods. `FileSource` inherits from that class and serves as a base for further classes to handle specific file formats (such as `CsvSource` and `TxtSource`).


### Notes
- `@abstractmethod` obligates all classes that inherit from it to have this specific method.
- [PEP 3119](https://peps.python.org/pep-3119/)




