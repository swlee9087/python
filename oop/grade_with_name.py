'''
name, 국어kor 영어eng 수학math 입력받아서
name, 총점, 평균, 학점 출력.

'''


class Grade(object):

    def __int__(self, name):
        self.name = name
        self.scores = []

    def addScores(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)


    @staticmethod
    def main():
        grade = Grade(input('Input Student Name : '))

        for i in ['Korean', 'English', 'Math']:
            grade.addScores(int(input(f'{i}: ')))

        avg = grade.avg()

        if avg >= 90:
            result = 'A'
        elif avg >= 80:
            result = 'B'
        elif avg >= 70:
            result = 'C'
        elif avg >= 60:
            result = 'D'
        elif avg <= 50:
            result = 'E'
        else:
            result = 'F'
        print(f'{result}')


Grade.main()
