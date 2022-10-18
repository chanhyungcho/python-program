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
from audioop import avg
from functools import total_ordering
from msilib import schema
from typing_extensions import Self
from unicodedata import name


class Grade(object):
    def __init__(self,name,nl,en,mt,total,avg,grade) -> None:
        self.name = name
        self.nl = nl
        self.en = en
        self.mt = mt
        self.total = total
        self.avg = avg
        self.grade = ""

    def execute(self):
        self.grade = self.get_Grade()
        self.get_grade()
        self.print_grade()

    def get_total(self):
        total = self.nl + self.en + self.mt
        return total

    def get_avg(self):
        avg = self.get_total() / 3
        return avg

    def get_grade(self):
        grade = ""
        avg = self.get_avg()
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "E"
        else:
            grade = "F" 

    def print_grade(self):
        name = self.name
        nl = self.nl
        en = self.en
        mt = self.mt
        total = self.total
        avg = self.avg
        grade = self.grade
        title = "### 성적표 ###"
        aster = "*"*40
        schema = "이름 국어 영어 수학 총점 평균 학점"
        result = f"{name} {nl} {en} {mt} {total} {avg} {grade}"
        print(f'{title} \n {aster} \n {schema} \n {aster} \n {result} {aster}')

    @staticmethod
    def main():
        name = input("이름: ")
        nl = int(input("국어: "))
        en = int(input("영어: "))
        mt = int(input("수학: "))
        total = total()
        avg = avg()
        grade = Grade(name, nl, en, mt, total, avg, grade)
        grade.execute()

Grade.main()

