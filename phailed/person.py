'''
이름 나이 주소 입력받아 자기소개 프그 작성
출력; 안녕하세요, 제이름은 Tom이고 나이는 28세이고, 서울에서 거주합니다.
여러사람 전부 입력받아 전체 일괄출력되는 시스템.
'''


class Person(object):

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):
        print(f'Name is {self.name}, Age is {self.age}, Address is {self.address}.\n')


def main():
    persons = []
    while 1:
        print('0-exit 1-add 2-print')
        menu = input('choice: ')
        if menu == '0':
            return
        elif menu == '1':
            persons.append(Person(input('name - '), input('age - '), input('address - ')))
        elif menu == '2':
            for i in persons:
                i.to_string()


if __name__ == '__main__':
    main()
