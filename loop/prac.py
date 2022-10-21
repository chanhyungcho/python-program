'''
아이디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 배발하시오.
'''
class Member(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name

    def print_info(self):
        print(self.id, self.pw, self.name)

    @staticmethod
    def print_member(ls):
        [i.print_info() for i in ls]

    @staticmethod
    def get_member():
        id = input("아이디: ")
        pw = input("비밀번호: ")
        name = input("이름: ")
        return Member(id, pw, name)

    @staticmethod
    def print_menu():
        print("1번메뉴: 가입")
        print("2번메뉴: 목록")
        print("3번메뉴: 탈퇴")
        print("4번메뉴: 종료")
        menu = input("메뉴번호 입력: ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print(" ### 가입 ### ")
                member = Member.get_member()
                ls.append(member)
            elif menu == 2:
                print(" ### 목록 ### ")
                member.print_member(ls)
            elif menu == 3:
                print(" ### 탈퇴 ### ")
            elif menu == 4:
                print(" ### 종료 ### ")
                break
            else: print("잘못된 메뉴번호 입니다.")

Member.main()