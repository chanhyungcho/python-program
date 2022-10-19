import random
from re import I
class Bubble(object):
    def __init__(self) -> None:
        pass

    def extract_random(self):
        return random.sample(range(1,101), 10)

    def print_random(self):
        for i in self.extract_random():
            if i % 2 == 0:
                print (i)

    @staticmethod
    def main():
        bubble=Bubble()
        bubble.extract_random()
        bubble.print_random()

Bubble.main()
