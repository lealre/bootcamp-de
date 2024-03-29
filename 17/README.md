# Day 17 - SQLAlchemy: Set of tools for manipulating SQL in Python

The objective is to create two relational tables using SQLAlchemy, insert their values, and consult them. We then perform a query to group products by suppliers and calculate the sum of prices for each product.

### Notes
- ORM - Object Relational Mapping
- `pyodbc` is a driver used to connect with a databse, and `sqlalchemy` uses it.
- Dialect 
    ```
    postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase
    ==
    {database}+{driver_to_connect_database}://{database_user}:{databse_pass}@{localhost/adress}/{database_name}
    ```
- DBAPI - [PEP 249](https://peps.python.org/pep-0249/) - This API has been defined to encourage similarity between the Python modules that are used to access databases
- Pool - Connections limit at same time.

![](image.png)

-----------------------
[Exaclidraw link](https://app.excalidraw.com/l/8pvW6zbNUnD/3tmGeQYjxeG)

[Class Repository](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/bootcamp/aula17)