from pandas import read_excel, DataFrame, ExcelWriter, concat
class Model:
    def __init__(self, working_file):
        self.workFile = working_file
        self.excel = read_excel(working_file, engine="openpyxl")
        self.columns = ["ID","Вид материала", "Размер катушки / вес, кг", "Сечение", "Цвет", "Условия хранения", "Статус", "Остаток"]

    def add_row(self, data):
        if len(self.excel["ID"]) == 0:
            id = 0
        else:
            id = self.excel["ID"].max() + 1
        dfData = {i: [j] for i, j in zip(self.columns[1:], data)}
        dfData["ID"] = [id]
        df = DataFrame(dfData)
        newDF = concat([self.excel, df])
        self.excel = newDF
        self.excel.reset_index(drop=True, inplace=True)
        return newDF

    def get_data(self, **filters):
        if not filters:
            return [self.columns, *self.excel.values.tolist()]
        else:
            return self.get_filtred_rows(**filters)
    
    def save(self):
        with ExcelWriter(self.workFile) as writer:
            self.excel.to_excel(writer, sheet_name="Лист 1", index=False)

    def get_filtred_rows(self, **kvargs):
        data = self.excel.values.tolist()
        dictedData = [dict(zip(self.columns, i)) for i in data]
        if color := kvargs.get("color"):
            dictedData = [i for i in dictedData if i["Цвет"] == color]

        if id := kvargs.get("ID"):
            dictedData = [i for i in dictedData if i["ID"] == int(id)]

        if material_type := kvargs.get("material_type"):
            dictedData = [i for i in dictedData if i["Вид материала"] == material_type]

        if weihgt := kvargs.get("weight"):
            dictedData = [i for i in dictedData if i["Размер катушки / вес, кг"] == weihgt]
        
        if conds := kvargs.get("conds"):
            dictedData = [i for i in dictedData if i["Условия хранения"] == conds]

        if status := kvargs.get("status"):
            dictedData = [i for i in dictedData if i["Статус"] == status]

        if width := kvargs.get("width"):
            dictedData = [i for i in dictedData if i["Сечение"] == width]

        if rest := kvargs.get("rest"):
            dictedData = [i for i in dictedData if i["Остаток"] == rest]
        
        filtredData = [self.columns, *[list(i.values()) for i in dictedData]]

        return filtredData
 
    def editRow(self, amount: int, rowID: int, operation: str):
        #row_index = self.excel[self.excel["ID"] == rowID].index
        rest = self.excel.loc[rowID, "Остаток"]
        if operation == "substract" and rest.astype(int) < amount:
            return "UNABLE TO PROCEED"
        elif operation == "substract" and rest.astype(int) >= amount:
            self.excel.loc[rowID, "Остаток"] = rest.astype(int) - amount
        elif operation == "add":
            self.excel.loc[rowID, "Остаток"] = rest.astype(int) + amount

        print(self.excel.loc[rowID, "Остаток"])
        self.update_status(rowID=rowID, rest=int(rest))

    def get_data_length(self, **filters):
        return len(self.get_data(**filters))

    def get_row_data(self, rowID: int):
        return self.excel.iloc[rowID].values.tolist()
    
    def update_status(self, rowID: int, rest: int):
        if rest == 0:
            self.excel.loc[rowID, "Статус"] = "Нет в наличии"
        elif rest <= 300:
            self.excel.loc[rowID, "Статус"] = "Используется"
        else:
            self.excel.loc[rowID, "Статус"] = "Добавлен"

    def get_dropdown_elements(self):
        out = []
        data = self.excel.values.tolist()
        dictedData = [dict(zip(self.columns, i)) for i in data]
        for i in dictedData:
            out.append(f"{i['ID']} | {i['Вид материала']} | {i['Цвет']}")

        return out