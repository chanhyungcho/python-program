from random_list import RandomList

class Odd_Even(object):
    def __init__(self) -> None:
        pass

    def print(self):
        r1 = RandomList()
        print(r1.get_random(1,10,3))
        for i in r1.get_random(10,100,10):
            if i % 2 == 0:
                print(f"짝수: {i}")
            else:
                print(f"홀수: {i} ")

'''
    @staticmethod
    def main():
        oe = Odd_Even()
        oe.print()
'''
if __name__ == "__main__":
    oe = Odd_Even()
    oe.print()

Odd_Even.main()