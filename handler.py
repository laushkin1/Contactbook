from classes import AddressBook, Name, Phone, Record, Birthday

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact is missing.'
        except ValueError:
            return 'Write numbers as phone please.'
        except IndexError:
            return 'Give me name and phone please.'
        except TypeError:
            return 'Error of arguments in function.'
    return inner


contacts = AddressBook('data.bin')


@input_error
def add(name: str, phone_number: str, birthday: str =None) -> str:
    phones = Phone(phone_number)
    phones = phones.make_list(phone_number)
    phones = [Phone(val) for val in phones]
    record = Record(name=Name(name), phones=phones, birthday=birthday)
    contacts.add_record(record)
    return f'Done, contact is saved.'


@input_error
def change(name: str, new_phone: str) -> str:
    record = contacts.get_records(name)
    phones = Phone(new_phone)
    phones = phones.make_list(new_phone)
    phones = [Phone(val) for val in phones]
    record.change_phone(phones)
    return 'Done, number is changed.'


@input_error
def phone(name: str) -> str:
    search(name)
    return f'\nThese are all phone numbers that match with \'{name}\'.'


def show() -> str:
    if len(contacts.records) == 0:
        return 'You have not any contacts.'
    else:
        return contacts.show_adb()


@input_error
def birthday(name: str) -> str:
    try:
        a = contacts.get_records(name)
        return f'{a.days_to_birthday()} days left'
    except:
        return 'This contact doesn\'t exist or has no birthday.'


@input_error
def search(value: str) -> str:
    if contacts.search(value) != {}:
        for name, numbers in contacts.search(value).items():
            print(f'  {name} :')
            for i in range(0, len(numbers)):
                print(f'    {i + 1}: {numbers[i]}')
        return '\nThese are all contacts.'
    return 'Nothing was found for your search.'

@input_error
def delete(username: str) -> str:
    if username == 'all':

        records_names = []
        for name, record in contacts.records.items():
            records_names.append(name)

        for name in records_names:
            record = contacts.get_records(name)
            contacts.delete_record(record)

        return 'All users deleted successfully'

    record = contacts.get_records(username)
    contacts.delete_record(record)
    return 'User deleted successfully'
