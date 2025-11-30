from view.view import TestView
from model.model import Model
import re
from datetime import datetime

class TestPresenter:
    def __init__(self, working_file):
        self.model = Model(working_file)
        self.view = TestView(self)
        self.fields = ["Вид материала", "Размер катушки / вес, кг", "Сечение", "Цвет", "Условия хранения", "Статус", "Остаток"]
        self.view.mainloop()
    
    #def upload_file(self, filepath: str) -> str:
    #    responce = self.model.setup(filepath)
    #    return responce

    def get_row(self, rowID: int):
        return self.model.get_row_data(rowID=rowID)

    def validate_row_data(self, data):
        # ["Вид материала", "Размер катушки / вес, кг", "Сечение", "Цвет", "Условия хранения", "Статус", "Остаток"]
        errors = []
        if not self.parse_size(data[1]):
            errors.append({"name": "Размер катушки / вес, кг - данные должны быть в формате Вес / Размер", "ind": 1})
        if not self.parse_diameter(data[2]):
            errors.append({"name": "Сечение - Значение должно быть числом", "ind": 2})
        if not data[6].replace("г", "").isdigit():
            errors.append({"name": "Остаток - Значение должно быть натуральным числом", "ind": 6})
        return errors

    def get_data_length(self, **filters):
        return self.model.get_data_length(**filters)

    def get_data(self, start_index: int, per_page: int, **filters):
        responce = self.model.get_data(**filters)[start_index:per_page+1]
        return responce
    
    def add_row(self, data):
        errors = []

        if not all(data):
            for num, i in enumerate(zip(self.fields,data)):
                if i[1] == "":
                    errors.append({"name": f"{i[0]} - Обязательное поле", "ind": num})

            return {"status": "error", "detail": errors}
        else:
            val_errors = self.validate_row_data(data)
            if len(val_errors) > 0:
                return {"status": "error", "detail": val_errors}
            parsedData = [
                data[0],
                data[1],
                self.parse_diameter(data[2]),
                data[3],
                data[4],
                data[5],
                self.parse_weight(data[6])
            ]
            self.validate_row_data(data)
            responce = self.model.add_row(parsedData)
            return {"status": "success", "data": responce}

    def filter_data(self, **filters):
        responce = self.model.get_filtred_rows(**filters)
        return responce

    def edit_row(self, rowID: int, amount: int, operation: str):
        if rowID == None:
            return {"status": "error", "detail": "Сначала выберите элемент"}
        try:
            float(amount)
            int(amount)
        except ValueError:
            return {"status": "error", "detail": "Списание или Пополнение должно быть числом"}
        if int(amount) <= 0:
            return {"status": "error", "detail": "Списание или Пополнение должно быть больше нуля"}
        return self.model.editRow(amount=int(amount), rowID=rowID, operation=operation)

    def save(self):
        self.model.save()

    def get_data_combobox(self):
        return self.model.get_dropdown_elements()
    
    def parse_weight(self, data: str):
        numbers = re.findall(r'\d+\.?\d*', data)
        if len(numbers) > 0:
            if "кг" in data.lower():
                weightNum = int(float(numbers[0]) * 1000)
            else:
                weightNum = int(numbers[0])

            return weightNum
        else:
            return False

    def parse_diameter(self, data: str):
        numbers = re.findall(r'\d+\.?\d*', data)
        if len(numbers) > 0:
            print(numbers[0])
            if float(numbers[0]) <= 0:
                return False
            return float(numbers[0])
        else:
            return False
    
    def parse_size(self, data: str):
        splittedData = data.split("/")
        if len(splittedData) == 1:
            return False
        weight, diameter = map(str.strip, splittedData)
        parsedWeight, parsedDiameter = self.parse_weight(weight), self.parse_diameter(diameter)
        #print(parsedWeight, parsedDiameter)
        if all([parsedWeight, parsedDiameter]):
            return parsedWeight, parsedDiameter
        else:
            return False
        
    def prepare_date(self):
        return datetime.now().strftime("%d.%m.%Y")