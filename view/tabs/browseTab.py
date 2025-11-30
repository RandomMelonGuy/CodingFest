from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkEntry, CTkComboBox, CTkTextbox, END
from CTkTable import CTkTable
from CTkMessagebox import CTkMessagebox

class BrowseTab(CTkFrame):
    def __init__(self, presenter, master: CTkFrame):
        self.presenter = presenter
        self.master = master
        self.per_page = 3
        self.curIndex = 0
        self.headers = ["ID", "Дата", "Материал", "Вес/Размер", "Сечение", "Цвет", "Хранение", "Статус", "Ост."]
        self.filterList = {}
        self.setupUI()
        
    
    def ChangingTable_next(self): 
        """Обновление данных в таблице"""
        dataLength = self.presenter.get_data_length(**self.filterList)
        if self.curIndex + self.per_page < dataLength:
            self.curIndex += self.per_page
            data = self.presenter.get_data(self.curIndex, self.curIndex + self.per_page, **self.filterList)
            self.table.configure(values=[self.headers] + data[1:])

    def ChangingTable_back(self): 
        """Обновление данных в таблице"""
        if self.curIndex - self.per_page >= 0:
            data = self.presenter.get_data(self.curIndex - self.per_page, self.curIndex, **self.filterList)
            self.curIndex -= self.per_page
            self.table.configure(values=[self.headers] + data[1:])

    def setupUI(self):
        self.values = self.presenter.get_data(self.curIndex, self.curIndex + self.per_page)
        self.table = CTkTable(master=self.master, values=self.values, command=self.view_info)
        self.table.pack(expand=True, fill="both", padx=20, pady=20)
        self.tab2_button_1 = CTkButton(self.master, width=1, text=">", command=self.ChangingTable_next) #Вперёд
        self.tab2_button_1.place(y=105, x=590)
        self.tab2_button_2 = CTkButton(self.master, width=1, text="<", command=self.ChangingTable_back) #Назад
        self.tab2_button_2.place(y=105, x=-1)

        self.tab2_lable = CTkLabel(self.master, text='ID')
        self.tab2_lable.place(y=5, x=40)
        self.tab2_entry = CTkTextbox(self.master, height=10, width=40, wrap="none")
        self.tab2_entry.place(y=5, x=60)
        self.tab2_lable_1 = CTkLabel(self.master, text='Вид материала')
        self.tab2_lable_1.place(y=5, x=120)
        self.tab2_entry_1 = CTkTextbox(self.master, height=10, width=40, wrap="none")
        self.tab2_entry_1.place(y=5, x=220)
        self.tab2_lable_2 = CTkLabel(self.master, text='Цвет')
        self.tab2_lable_2.place(y=5, x=280)
        self.tab2_entry_2 = CTkTextbox(self.master, height=10, width=40, wrap="none")
        self.tab2_entry_2.place(y=5, x=315)
        self.tab2_lable_3 = CTkLabel(self.master, text='Статус')
        self.tab2_lable_3.place(y=5, x=375)
        self.tab2_entry_3 = CTkTextbox(self.master, height=10, width=40, wrap="none")
        self.tab2_entry_3.place(y=5, x=425)


        self.applyBtn = CTkButton(self.master, width=30, height=10, text="Применить", command=self.apply_filters)
        self.applyBtn.place(x=475, y=8)

    def setupData(self):
        self.values = self.presenter.get_data(self.curIndex, self.curIndex + self.per_page)
        self.table.configure(values=[self.headers] + self.values[1:])

    def apply_filters(self):
        self.curIndex = 0
        filters = [self.tab2_entry.get("0.0", END).replace("\n", ""), self.tab2_entry_1.get("0.0", END).replace("\n", ""), self.tab2_entry_2.get("0.0", END).replace("\n", ""), self.tab2_entry_3.get("0.0", END).replace("\n", "")]
        columns =  ["ID","material_type", "color", "status"]
        dictedData = dict(zip(columns, filters))
        filterParams = {key: value for key, value in dictedData.items() if value != ""}
        self.filterList = filterParams
        filtredData = self.presenter.get_data(start_index=self.curIndex, per_page=self.per_page,**filterParams)
        self.table.configure(values=filtredData)

    def view_info(self, row):
        data = map(str, self.values[row["row"]])
        params = dict(zip(self.headers, data))
        text = ""
        for key, value in params.items():
            text += f"• {key} - {value}\n"
        CTkMessagebox(master=self.master, title="VIEW", message=text)
        