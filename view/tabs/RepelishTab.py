from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkComboBox, CTkEntry
from CTkMessagebox import CTkMessagebox

class RepelishTab(CTkFrame):
    def __init__(self, master, presenter):
        self.master = master
        self.presenter = presenter
        self.rowID = None
        self.data = []
        self.setupUI()
    
    #def update_data(self):
    #    self.up

    def setupUI(self):
        self.combo = CTkComboBox(self.master, values=self.data, command=self.on_select, width=225, height=35)
        self.combo.pack(padx=20, pady=20)
        self.combo.set("Выберите материал")

        self.entry = CTkEntry(self.master)
        self.entry.place(x=450, y=20)
        self.tab3_button_1 = CTkButton(self.master, text='Пополнить', command=self.add)
        self.tab3_button_1.place(x=450, y=50)
        self.tab3_button_2 = CTkButton(self.master, text='Списать', command=self.substract)
        self.tab3_button_2.place(x=450, y=80)

    def on_select(self, choice):
        self.rowID = int(choice.split("|")[0].strip())
        self.update_label(self.rowID)

    def add(self):
        amount = self.entry.get()
        responce = self.presenter.edit_row(rowID=self.rowID, amount=amount, operation="add")
        if responce is not None:
            CTkMessagebox(title="ERROR", message=responce["detail"], icon="cancel")
        else:
            self.update_combo()
            self.update_label(self.rowID) # type: ignore
    
    def substract(self):
        amount = self.entry.get()
        responce = self.presenter.edit_row(rowID=self.rowID, amount=amount, operation="substract")
        if responce is not None:
            CTkMessagebox(title="ERROR", message=responce["detail"], icon="cancel")
        else:
            self.update_combo()
            self.update_label(self.rowID)

    def update_label(self,rowID: int):
        data = self.presenter.get_row(rowID=rowID)
        if not hasattr(self, 'tab3_label'):
            self.tab3_label = CTkLabel(self.master, text=" ")
            self.tab3_label.place(x=265, y=55)

            self.tab3_label_1 = CTkLabel(self.master, text=" ")
            self.tab3_label_1.place(x=265, y=75)

            self.tab3_label_2 = CTkLabel(self.master, text=" ")
            self.tab3_label_2.place(x=265, y=95)

            self.tab3_label_3 = CTkLabel(self.master, text=" ")
            self.tab3_label_3.place(x=265, y=115)

            self.tab3_label_4 = CTkLabel(self.master, text=" ")
            self.tab3_label_4.place(x=265, y=135)
        
        print(data)

        self.tab3_label.configure(text=f"Тип: {data[2]}")
        self.tab3_label_1.configure(text=f"Цвет: {data[5]}")
        self.tab3_label_2.configure(text=f"Сечение: {data[4]}")
        self.tab3_label_3.configure(text=f"Вес катушки: {data[3]}")
        self.tab3_label_4.configure(text=f"Остаток: {data[-1]}")

    def update_combo(self):
        data = self.presenter.get_data_combobox()
        self.combo.configure(values=data)