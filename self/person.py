class Person(object):

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):
        print(f'\nPersonal File: \n'
              f'Name - {self.name}\n'
              f'Age - {self.age}\n'
              f'Address - {self.address}\n')


def main():
    persons = []
    while 1:
        print('\n 0-exit 1-add 2-list')
        menu = input('choose 1. ')

        if menu == '1':
            persons.append(Person(input('name'), input('age'), input('address')))
        elif menu == '2':
            for i in persons:
                i.to_string()
        elif menu == '0':
            return


if __name__ == '__main__':
    main()
