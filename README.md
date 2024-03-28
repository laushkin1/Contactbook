# Contactbook
This is my first project made with vanila python in 22.04.2023

## How to use?
You can simply skip to the last step, but if you have any problems, use the entire manual

1. First you need to make virtual environment with python
```bash
python -m venv env
source env/bin/activate
```

2. After that you need to install all requirements from [requirements.txt](requirements.txt)
```bash
pip install -r requirements.txt
```

3. Finaly you can run program by
```bash
python main.py
```

## Comands
`help` - Command that shows all commands

`add` - Add a user to your ContactBook

`change` - Change phone of your contact

`phone` - Search user by phone

`show` - Show all users in your ContactBook

`birthday` - Show how many days left to birthday

`search` - Search user by name or phone number

`delete` - Delete user by name

`close` or `exit` - Close program

#

- `help` - Command used without any arguments
    ```bash
    help
    ```
    Command that shows all commands

- `add` - Command used with 2 or 3 arguments separated by comma
    ```bash
    add Name Surname, phonenumber1 phonenumber2, birthday
    ```
    Please note that you can have as many phone numbers as you like, but the date of birth must be in the following form dd.mm.yyyy

    For example
    ```bash
    add Ken Thompson, 123 456 789, 01.01.1970
    add Dennis Ritchie, 0987654321
    ```
    Here, Ken Thompson has three phone numbers and a date of birth, but Dennis Ritchie has one phone number and no birthday 

- `change` - Command used with 2 arguments separated by comma
    ```bash
    change Name Surname, phonenumber1 phonenumber2
    ```
    Notice that you need wtrite whole name correctly. After the command is executed, all user phone numbers will be deleted and replaced with the ones you entered

- `phone` - Command used with 1 argument
    ```bash
    phone 123
    ```
    After executing the command, you will be shown all users with matching phone numbers

- `show` - Command used without any arguments
    ```bash
    show
    ```

- `birthday` - Command used with 1 argument
    ```bash
    birthday Ken Thompson
    ```
    Notice that you need wtrite whole name correctly, the function will return the number of days left until the user's birthday

- `search` - Command used with 1 argument
    ```bash
    search Name
    search PhoneNumber
    ```
    The function returns all users that match the argument

 - `delete` - Command used with 1 argument
    ```bash
    delete username
    ```
    You can also delete all users at once using the folowing argument
    ```bash
    delete all
    ```

## Author
- [@laushkin1](https://github.com/laushkin1)
