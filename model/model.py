from random import randint

class Model:
    def get_random(self, maxVal: int) -> int:
        return randint(1,maxVal)