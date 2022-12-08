from random_list import RandomList

class Odd_Even(object):
    def __init__(self) -> None:
        pass

    def print(self):
                r1 = RandomList()
               print([f"짝수: {i}" if i % 2 == 0 else f"홀수: {i} " for i in r1.get_random(10,100,10)])



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