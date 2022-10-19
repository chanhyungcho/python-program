import random

class RandomList(object):
    
    def __init__(self) -> None:
        pass

    def get_random(self, start, end, count):
        return random.sample(range(start, end), k = count)    #getter

    def print(self):
        print(self.get_random(10, 100, 10))
'''
    @staticmethod
    def main():
        r1=RandomList()    #wrapping에서 뺀것(클래스 밖으로 뺀 것.)
        r1.print()

RandomList.main()
'''

if __name__=="__main__":
    r1 = RandomList()
    r1.print()