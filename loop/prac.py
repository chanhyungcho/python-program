from curses import pair_number


class Contact(object):
    def __init__(self,name,pnum,mail,addr) -> None:
        self.name = name
        self.pnum = pnum
        self.mail = addr
        self.mail = mail

    @staticmethod
    def new_contact():
        name = (input("이름:"))
        pnum = (input("번호:"))
        mail = (input("메일:"))
        addr = (input("주소:"))
        return Contact(name,pnum,mail,addr)

    def print_info(self):
        print(f"{self.name}, {self.pnum}, {self.mail}, {self.addr}")

    @staticmethod
    def get_contact():
        for i in 

    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴 선택: ")
        return int(menu)