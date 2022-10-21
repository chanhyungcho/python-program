"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
********************************
"""

class Prac(object):
    def __init__(self,name,ko,en,ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.grade = ""

    def get_total(self):
        self.total = self.ko + self.en + self.ma
        return self.total

    def get_avg(self):
        self.avg = self.total / 3
        return self.avg

    def get_grade(self):
        avg = self.avg
        if avg >= 90:
            result = "A"
        elif avg >= 80:
            result = "B"
        elif avg >= 70:
            result = "C"
        elif avg >= 60:
            result = "D"
        elif avg >= 50:
            result = "E"
        else:
            result = "F"
        self.grade = result

    def print_grade(self):
        print("### 성적표 ###")
        print("********************************")
        print("이름 국어 영어 수학 총점 평균 학점")
        print("********************************")
        print(f"{self.name} {self.ko} {self.en} {self.ma} {self.total} {self.avg} {self.grade}")
        print("********************************")

    @staticmethod


    @staticmethod
    def main():
        ls = []
        while True:
            name = input("이름: ")
            ko = int(input("국어:"))
            en = int(input("영어:"))
            ma = int(input("수학:"))
            pr = Prac(name,ko,en,ma)
            pr.get_total()
            pr.get_avg()
            pr.get_grade()
            pr.print_grade()

Prac.main()