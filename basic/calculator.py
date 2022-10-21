class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        num1 = self.num1
        op = self.op
        num2 =self.num2
        if op == "+": 
           result = num1 + num2
        elif op == "-":
           result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:
            result = "잘못된 연산입니다."
        print(f"{num1} {op} {num2} = {result}")

    @staticmethod
    def print_menu():
            num1 = int(input("숫자 : "))
            op = input("+, -, *, /, %")
            num2 = int(input("숫자 : "))
            calculator = Calculator(num1, op, num2)
            calculator.calc()

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Calculator.print_menu()
            if menu == 0: break
            elif menu == 1:
                print("등록") #CRUD create read update delect
            elif menu == 2:
                print("목록")
            elif menu == 3:
                print("삭제")
            else: print("없는 메뉴입니다. 다시 선택해주세요.")



Calculator.main()

  