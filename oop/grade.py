class Grade(object):

    def __int__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    @staticmethod
    def main():
        kor = int(input('Korean : '))
        eng = int(input('English : '))
        math = int(input('Math : '))
        grade = Grade(kor, eng, math)
        avg = grade.avg()

        if avg >= 90:
            result = 'A'
        elif avg >= 80:
            result = 'B'
        elif avg >= 70:
            result = 'C'
        elif avg >= 60:
            result = 'D'
        elif avg >= 50:
            result = 'E'
        else:
            result = 'F'
        print(f'{result}')


Grade.main()
