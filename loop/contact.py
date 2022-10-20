'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인원은 여러명 저장 가능합니다.
'''

class Contact(object):
    def __init__(self,name,pnum,email,add) -> None:
        self.name = name
        self.pnum = pnum
        self.email = email
        self.add = add

    @staticmethod
    def new_contact():
        name = input("이름:")
        pnum = input("전화번호:")
        email = input("이메일:")
        add = input("주소:")
        return Contact(name,pnum,email,add)

    def print_info(self):
         print(f"{self.name}, {self.pnum}, {self.email}, {self.add}")

    @staticmethod
    def get_contacts(ls):
        for i in ls:
            i.print_info()
        
    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴 선택: ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print("###연락처 등록###")
                contact = Contact.new_contact()
                ls.append(contact) #덧붙이다, 첨부하다 / [ ]에 추가할 때는 append
            elif menu == 2:
                print("###연락처 출력###")
                Contact.get_contacts(ls)
            elif menu == 3:
                print("###연락처 삭제###")
            elif menu == 4:
                print(" 주소록 어플을 종료합니다...")
                break

Contact.main()