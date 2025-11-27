from customtkinter import CTkEntry, CTkLabel, CTkFrame

class AddTab(CTkFrame):
    def __init__(self, tabComponent: CTkFrame, presenter):
        self.presenter = presenter
        self.tab = tabComponent
        self.setupUI()
    
    def setupUI(self):
        self.tab_label = CTkLabel(self.tab, text = "Обязательно заполните все поля.")
        self.tab_label.pack(pady=5)
        self.tab_material = CTkEntry(self.tab, height=60, width=85)
        self.tab_material.place(y=55, x=5)
        self.tab_form = CTkEntry(self.tab, height=60, width=85)
        self.tab_form.place(y=55, x=90)
        self.tab_section = CTkEntry(self.tab, height=60, width=85)
        self.tab_section.place(y=55, x=175)
        self.tab_color = CTkEntry(self.tab, height=60, width=85)
        self.tab_color.place(y=55, x=260)
        self.tab_storage = CTkEntry(self.tab, height=60, width=85)
        self.tab_storage.place(y=55, x=345)
        self.tab_status = CTkEntry(self.tab, height=60, width=85)
        self.tab_status.place(y=55, x=430)
        self.tab_balance = CTkEntry(self.tab, height=60, width=85)
        self.tab_balance.place(y=55, x=515)

        self.tab_label_1 = CTkLabel(self.tab, text="Вид материала")
        self.tab_label_1.place(y=26, x=2)
        self.tab_label_2 = CTkLabel(self.tab, text="Размер/Вес")
        self.tab_label_2.place(y=26, x=98)
        self.tab_label_3 = CTkLabel(self.tab, text="Сечение")
        self.tab_label_3.place(y=26, x=192)
        self.tab_label_4 = CTkLabel(self.tab, text="Цвет")
        self.tab_label_4.place(y=26, x=287)
        self.tab_label_5 = CTkLabel(self.tab, text="Усл.Хранения")
        self.tab_label_5.place(y=26, x=345)
        self.tab_label_6 = CTkLabel(self.tab, text="Статус")
        self.tab_label_6.place(y=26, x=450)
        self.tab_label_7 = CTkLabel(self.tab, text="Остаток")
        self.tab_label_7.place(y=26, x=530)