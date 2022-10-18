"""
이름, 주민번호 (950101-1), 주소를 입력받아서 
회원명부를 관리하는 어플을 제작하고자 한다.

출력되는 결과는 다음과 같다.
### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25세 (만나이)
성별: 남성
주소: 서울
********************************
"""

from codecs import getencoder
from ctypes import addressof
from stat import SF_SNAPSHOT
from sys import set_asyncgen_hooks
from unicodedata import name


class Person(object):
    def __init__(self,name,ssn,address) -> None:
        self.name = name
        self.ssn = ssn
        self.address = address
        self.age = 0
        self.gender = ""
      
    def set_age(self):
        current = 2022
        year = int(self.ssn[:2]) #인덱스 0,1은 출생년도
        gender_checker = int(self.ssn[7]) #7은 성별판별번호 인덱스
        if gender_checker == 1 or gender_checker == 2:
            year += 1900
            if gender_checker ==1:
                self.gender = "남성"
            else:
                self.gender = "여성"
        elif gender_checker == 3 or gender_checker == 4:
            year += 2000
            if gender_checker ==3:
                self.gender = "남성"
            else:
                self.gender = "여성"
        self.age = current - year


    def set_gender(self):
        self.gender = ""
        d = int(self.ssn[8])
        e = ""
        if 
        
   
        
    def print_person(self):
        print("### 자기소개어플 ###")
        print("********************************")
        print(f"이름: {self.name}")
        print(f"나이: {self.age}(만나이)")
        print(f"성별: {self.gender}")
        print(f"주소: {self.address}")
        print("********************************")


    @staticmethod
    def main():
        name = input("이름: ")
        ssn = input("주민번호: ")
        address = input("주소: ")
        person = Person(name,ssn,address)
        person.set_age()
        person.set_gender()
        person.print_person()
Person.main()

