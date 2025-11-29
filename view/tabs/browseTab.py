from customtkinter import CTkFrame, CTkButton
from CTkTable import CTkTable

class BrowseTab(CTkFrame):
    def __init__(self, presenter, master: CTkFrame):
        self.presenter = presenter
        self.master = master
        self.per_page = 3
        self.curIndex = 0
        self.setupUI()

    def ChangingTable_next(self): 
        """Обновление данных в таблице"""
        self.curIndex += self.per_page
        data = self.presenter.get_data(self.curIndex, self.curIndex + self.per_page)
        self.table.configure(values=data)

    def ChangingTable_back(self): 
        """Обновление данных в таблице"""
        data = self.presenter.get_data(self.curIndex - self.per_page, self.curIndex)
        self.curIndex -= self.per_page
        self.table.configure(values=data)
        print(f"Таблица обновлена")

    def setupUI(self):
        values = self.presenter.get_data(self.curIndex, self.curIndex + self.per_page)
        self.table = CTkTable(master=self.master, values=values)
        self.table.pack(expand=True, fill="both", padx=20, pady=20)
        self.tab2_button_1 = CTkButton(self.master, width=1, text=">", command=self.ChangingTable_next) #Вперёд
        self.tab2_button_1.place(y=105, x=590)
        self.tab2_button_2 = CTkButton(self.master, width=1, text="<", command=self.ChangingTable_back) #Назад
        self.tab2_button_2.place(y=105, x=-1)