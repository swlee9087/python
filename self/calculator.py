class Calculator(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def power(self):
        return self.num1 ** self.num2

    def modulo(self):
        return self.num1 % self.num2

    @staticmethod
    def again():
        calc_again = input('\nagain? Y/N ')
        if calc_again.upper() == 'Y':
            main()
        elif calc_again.upper() == 'N':
            print('Bye')
        else:
            Calculator.again()

def main():
    while 1:
        num1 = int(input('first num '))
        num2 = int(input('second num '))
        calc = Calculator(num1, num2)
        menu = input('\n menu > 0=exit | + | - | * | / | ^^ | modulo \n')

        if menu == '0':
            break
        elif menu == '+':
            print(f'{calc.num1}+{calc.num2}={calc.add()}')
            Calculator.again()
        elif menu == '-':
            print(f'{calc.num1}-{calc.num2}={calc.subtract()}')
            Calculator.again()
        elif menu == '*':
            print(f'{calc.num1}*{calc.num2}={calc.multiply()}')
            Calculator.again()
        elif menu == '/':
            print(f'{calc.num1}/{calc.num2}={calc.divide()}')
            Calculator.again()
        elif menu == '^^':
            print(f'{calc.num1}**{calc.num2}={calc.power()}')
            Calculator.again()
        elif menu == '6':
            print(f'{calc.num1}%{calc.num2}={calc.modulo()}')
            Calculator.again()
        else:
            print('Wrong input')
            Calculator.again()


main()

