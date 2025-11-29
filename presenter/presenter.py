from view.view import TestView
from model.model import Model

class TestPresenter:
    def __init__(self, working_file):
        self.model = Model(working_file)
        self.view = TestView(self)
        self.view.mainloop()
    
    #def upload_file(self, filepath: str) -> str:
    #    responce = self.model.setup(filepath)
    #    return responce
    
    def get_data(self, start_index: int, per_page: int):
        responce = self.model.get_data()[start_index:per_page+1]
        print(f"[{start_index}:{per_page}]")
        return responce
    
    def add_row(self, data):
        responce = self.model.add_row(data)
        return responce
    
    def filter_data(self, **filters):
        responce = self.model.get_filtred_rows(**filters)
        return responce

    def edit_row(self, rowID: int, amount: int, operation: str):
        return self.model.editRow(amount=amount, rowID=rowID, operation=operation)

    def save(self):
        self.model.save()