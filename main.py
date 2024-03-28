from handler import add, change, phone, show, contacts, birthday, search, delete

exit_commands = ['close', 'exit', '.']
help_commands = ['help', 'commands', '?']

dict_of_commands = {
        'add': add,
        'change': change,
        'phone': phone,
        'show': show,
        'birthday': birthday,
        'search': search,
        'delete': delete
}

while True:
    command, *date = input('\nEnter command: ').strip().split(' ', 1)
    command = command.lower()

    if command in exit_commands:
        contacts.serialize()
        print('Program ends')
        break

    elif dict_of_commands.get(command):
        handler = dict_of_commands.get(command)
        if date:
            date = date[0].split(', ')
            print(handler(*date))
        else:
            print(handler())

    elif command in help_commands:
        print(' This is list of command: \n')

        print(' `add` - Add a user to your ContactBook')
        print(' `change` - Change phone of your contact')
        print(' `phone` - Search user by phone')
        print(' `show` - Show all users in your ContactBook')
        print(' `birthday` - Show how many days left to birthday')
        print(' `search` - Search user by name or phone number')
        print(' `delete` - Delete user by name')
        print(' `close` or `exit` - Close program')

        print('\n for more information please read file README.md')
    else:
        print('Unknown command!')
