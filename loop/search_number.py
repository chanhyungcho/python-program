'''
두자리 정수 랜덤숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 계발하시오.
예) [23, 12, 48,...,]
사용자의 input 값이 12인 경우
출력값이 12, 48만 되도록 한다.
'''

from random_list import RandomList #랜덤 리스트 파일에서 랜덤 리스트 클래스를 가져옴
class SearchNumber(object): #클래스 이름 설정 및 객체 지향 프로그램으로 설정
    def __init__(self,num) -> None: #생성자 설정
        self.num = num #프로포티 설정 

    def print(self): #출력 메소드 설정
        r1 = RandomList() 
        num = self.num
        print(r1.get_random(11,100,10))
        for i in [r1.get_random(11,100,10)]:
            if i % num == 0:
                print (i)


    @staticmethod #데코레이터 패턴
    def main(): #
        num = int(input("숫자 : "))
        sn = SearchNumber(num)
        sn.print()

SearchNumber.main()