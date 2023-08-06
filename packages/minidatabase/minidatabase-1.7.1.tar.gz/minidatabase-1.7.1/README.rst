# Minidb Python Third-Party Database

Minidb is a Python third-party database that provides a simple and easy-to-use interface for creating, appending and managing databases. It allows for database creation and manipulation without having to use any complex SQL commands.

## Installation

To install Minidb, you can use pip by running the following command:

```
pip install minidatabase
```

## Usage

To start using minidb, you must first import the library by using the following command:

``` python
from minidatabase import minidb
```

### Creating a Database

To create a local database, you can use the `connect` method, which takes a single parameter, the path to the database. For example:

``` python
db = minidb.connect('example.minidb')
```

To create a WebMDB server database, you can use the `web_connect` method, which takes three parameters: password, server_address and port. You can start the server using the `minidb -w` command on the command line. You can then create a database using the `minidb -c example.minidb` command.

### Database Operations

After creating a cursor for the database, you can start using the various database operations. Here are some important ones:

#### Append Method

The append method is used to add data to the database. It takes two parameters, `tag` and `value`, and is used to create a new tag and assign it a value. For example:

``` python
db.append('name', 'John')
```

#### Delete Method

The delete method is used to delete an entry from the database by tag name. For example:

``` python
db.delete('name')
```

#### Search Method

The search method is used to search the database for a keyword. It returns a list of tags with matching keywords. For example:

``` python
db.search('age')
```

#### Search_value Method

The search_value method is used to search the database for a specific value. It returns a list of tags with matching values. For example:

``` python
db.search_value('John')
```

#### Search_tag Method

The search_tag method is used to search the database for a specific tag. It returns a list of tags with matching tag names. For example:

``` python
db.search_tag('name')
```

#### Clean Method

The clean method is used to clear the database. For example:

``` python
db.clean()
```

#### List Method

The list method is used to list all the entries in the database. For example:

``` python
db.list()
```

#### Commit Method

The commit method is used to save the changes made to the database. For example:

``` python
db.commit()
```

#### Close Method

The close method is used to close the database cursor. For example:

``` python
db.close()
```

## Contributions

Minidb welcomes and appreciates any contributions. If you find any bugs or have any suggestions for improvement, feel free to create a pull request or an issue in the repository.

## License

This project is licensed under the  GNU GENERAL PUBLIC LICENSE - see the `LICENSE` file for details.