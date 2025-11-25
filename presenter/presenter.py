from view.view import TestView
from model.model import Model

class TestPresenter:
    def __init__(self):
        self.model = Model()
        self.view = TestView(self)
        self.view.mainloop()

    def get_random(self, maxVal: int) -> int:
        return self.model.get_random(maxVal)
    