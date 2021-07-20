class Contact(object):

    def __init__(self, name, phone, email, address):  # inst factor designated
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')


def set_contact():
    return Contact(input('Name: '), input('Number: '), input('Email; '), input('Address: '))  # inst on RAM.


def get_contact(ls):  # print directly
    for i in ls:  # i=element, ls=obj
        i.to_string()


def del_contact(ls, name):
    for i, j in enumerate(ls):  # ??
        if i.name == name:
            del ls[i]


def print_menu(ls):
    for i, j in enumerate(ls):  # i=index element
        print(str(i) + '-' + j + '\t')
    return int(input())


def main():
    ls = []
    while 1:
        menu = print_menu(['exit', 'add', 'print', 'delete'])
        if menu == '1':
            t = set_contact()
            ls.append(t)
        elif menu == '2':
            get_contact(ls)
        elif menu == '3':
            del_contact(ls, input('Delete Contact'))
        else:
            return


if __name__ == '__main__':
    '''
    ls = ['exit', 'add', 'search', 'delete']
    ls2 = []
    '''
    main()
