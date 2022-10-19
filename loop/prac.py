'''
두자리 정수 랜덤숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 계발하시오.
예) [23, 12, 48,...,]
사용자의 input 값이 12인 경우
출력값이 12, 48만 되도록 한다.
'''

from random_list import RandomList

class Prac(object):
    def __init__(self,num) -> None:
        self.num = num

    def print(self):
        rl = RandomList()
        num = self.num
        r2 = rl.get_random(11,100,10)
        print(r2)
        for i in r2:
            if i % num == 0:
                print (i)

    @staticmethod
    def main():
        num = int(input("숫자: "))
        pr = Prac(num)
        pr.print()

Prac.main()
