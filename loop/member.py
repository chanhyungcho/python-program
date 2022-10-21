'''
아이디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발하시오.
'''

class Member(object):

    def __init__(self,id,pw,name):
        self.id = id
        self.pw = pw
        self.name = name

    def print_info(self):
        print(self.id, self.pw, self.name)

    @staticmethod
    def print_member(ls):
        [i.print_info() for i in ls]

    @staticmethod
    def new_member():
        id = input("아이디: ")
        pw = input("비밀번호: ")
        name = input("이름: ")
        return Member(id, pw, name)

    @staticmethod
    def print_menu():
        print("1.등록")
        print("2.출력")
        print("3.탈퇴")
        print("0.종료")
        menu = int("메뉴 선택: ")
        return menu(int)

    @staticmethod
    def delect_member(ls,name):
        for i, j in enumerate():
            if j.name == name:
                del ls[i]


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print("### 1.등록 ###")
                member = Member.new_member()
                ls.append(Member)
            elif menu == 2:
                print("### 2.목록 ###")
                Member.print_member(ls)
            elif menu == 3:
                print("### 3.탈퇴 ###")
                Member.delect_member(ls)
            elif menu == 0:
                print("### 종료 ###")
                break
            else:
                print("다시 선택하십시오")


Member.main()

