'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))
BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.
### 비만도 계산 ###
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
***************************
'''

class Bmi(object):
    def __init__(self, name, cm, kg) -> None:
        self.name = name
        self.cm = cm
        self.kg = kg
        self.biman = ""

    def execute(self):
        self.biman = self.get_biman()
        self.get_biman()
        self.print_biman()

    def get_bmi(self):
        kg = self.kg
        m = self.cm / 100
        return kg / m ** 2

    def get_biman(self):
        biman = ""
        bmi = self.get_bmi()
        if bmi >= 35:
            biman = "고도비만"
        elif bmi >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif bmi >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        self.biman = biman

    def print_biman(self):
        name = self.name
        cm = self.cm
        kg = self.kg
        biman = self.biman
        title = "### 비만도 계산 ###"
        aster = "*"*40
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        result = f"{name} {cm} {kg} {biman}"
        print(f'{title} \n {aster} \n {schema} \n {aster} \n {result} \n {aster} ')


    @staticmethod
    def print_menu():
        name = input("이름: ")
        cm = int(input("키: "))
        kg = int(input("몸무게: "))
        bmi = Bmi(name, cm, kg)
        bmi.execute()
        return int(input("메뉴: "))
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                print("1. Bmi등록")
            elif menu == 2:
                print("2. Bmi출력")
            elif menu == 3:
                print("3. Bmi삭제")
            elif menu == 4:
                print("4. 종료")
                break
            else: print("잘못된 접근입니다")



        
Bmi.main()