What is this?
-------------

LightDB is a simple and lightweight JSON database for Python that allows users to **efficiently** write data to a file. It is designed to be **easy to use**, making it a great choice for developers who need a fast and reliable way to store and retrieve data.


Features
--------

- Lightweight: LightDB is a lightweight database that is implemented as a Python dictionary, making it simple and easy to use.
- Simple API: LightDB provides a simple and intuitive API that allows users to easily set, get, and remove key-value pairs in the database.
- JSON file storage: LightDB stores its data in a JSON file, making it easy to read and edit the database outside of the Python environment.
- Nested dictionaries: LightDB supports nested dictionaries, allowing users to organize their data in a hierarchical structure.
- Persistance: LightDB's data is persisted in the JSON file, ensuring that it is retained between program runs.
- Reset: LightDB provides a reset method that allows users to clear the database and start fresh.
- Type agnostic: LightDB is type-agnostic, meaning it can store any Python object as a value in the database.
- Portable: LightDB can be easily transferred between different systems, making it a great choice for simple data storage needs.


Simple usage
------------

.. code-block:: python

    from lightdb import LightDB

    # Create a new database object, or load an existing one from file
    db = LightDB("my_database.json")

    # Set a key-value pair
    db.set("name", "Alice")

    # Get the value associated with a key
    name = db.get("name")
    print(name)  # Output: "Alice"

    # Set a key-value pair in a nested dictionary
    db.set_key("person", "age", 30)

    # Get the value associated with a key in a nested dictionary
    age = db.get_key("person", "age")
    print(age)  # Output: 30

    # Remove a key-value pair from the database
    db.pop("name")

    # Remove a key-value pair from a nested dictionary
    db.pop_key("person", "age")

    # Reset the database to an empty state
    db.reset()
