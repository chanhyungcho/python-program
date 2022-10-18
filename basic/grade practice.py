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

class Grade(object):
    def __init__(self,name,ko,en,ma) -> None:
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.total = 0
        self.avg = 0.0
        self.grade = ""

    def set_total(self):
        self.total = self.ko + self.en + self.ma
        return self.total

    def set_avg(self):
        self.avg = self.total / 3
        return self.avg

    def set_grade(self):
        if self.avg >= 90 