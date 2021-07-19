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


    def to_string(param):
        print(f'\n안녕하세요, 제 이름은 {param.name}이고, 나이는 {param.age}세이고, {param.address}에서 거주합니다.')

    @staticmethod
    def main():
        count = int(input('how many? '))

        for i in range(count):
            infos.append(Person)
            person = Person(input('name: '), input('age: '), input('address: '))
        for i in range(count):
            infos.append(Person.to_string(person))


Person.main()
