from view.view import TestView
from model.model import Model

class TestPresenter:
    def __init__(self, working_file):
        self.model = Model(working_file)
        self.view = TestView(self)
        self.view.mainloop()
    
    def upload_file(self, filepath: str) -> str:
        responce = self.model.setup(filepath)
        return responce
    
    def print_data(self):
        responce = self.model.print_data()
        return responce
    
    def add_row(self, data):
        responce = self.model.add_row(data)
        return responce
    
    def save(self):
        self.model.save()