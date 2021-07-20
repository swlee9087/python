class Contacts(object):

    def __init__(self, name, phone, email, address):  # inst factor designated
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')


def set_contact():
    return Contacts(input('Name: '), input('Number: '), input('Email; '), input('Address: '))
    # inst on RAM. name/number etc = 0D


def get_contact(ls):  # print directly
    for i in ls:  # i=element 1D, ls=obj 2D
        i.to_string()


def del_contact(ls, name):
    for i, j in enumerate(ls):  # i=index bc index needed for data coordinate
        if name == j.name:  # no 'switch' in py, so. i=fixed, j=variable
            del ls[i]


def print_menu(ls):  # ????
    t = ' '  # for-in cannot use join fn, so sep ln
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))
"""
ls = ['exit', 'add', 'search', 'delete']
    str = ' | '
    print(str.join(ls))"""

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
            break


if __name__ == '__main__':
    '''
    ls = ['exit', 'add', 'search', 'delete']
    ls2 = []
    '''
    main()
