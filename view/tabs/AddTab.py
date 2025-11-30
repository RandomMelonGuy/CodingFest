from customtkinter import CTkEntry, CTkLabel, CTkFrame, CTkButton
from CTkMessagebox import CTkMessagebox

class AddTab(CTkFrame):
    def __init__(self, tabComponent: CTkFrame, presenter):
        self.presenter = presenter
        self.tab = tabComponent
        self.tab.bind("<Leave>", lambda e: self.clear_all_highlighting())
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
        self.tab1_button_1 = CTkButton(self.tab, text = "Отправить", command=self.add_row)
        self.tab1_button_1.pack(pady=90)

        self.entries = [self.tab_material, self.tab_form, self.tab_section, self.tab_color, self.tab_storage, self.tab_status, self.tab_balance]
        self.setupEntries()

    def hightlight_fields(self, errors):
        for entry in errors:
            self.entries[entry["ind"]].configure(border_color="red")

    def setupEntries(self):
        for i in range(len(self.entries)):
            self.entries[i].bind("<FocusIn>", lambda e, i=i: self.clear_highlighting(i))

    def clear_highlighting(self, index):
        self.entries[index].configure(border_color="#85898B")

    def clear_all_highlighting(self):
        for i in range(len(self.entries)):
            self.clear_highlighting(i)

    def add_row(self):
        data = [i.get() for i in self.entries]
        responce = self.presenter.add_row(data)
        values = ""
        print(responce)
        if responce["status"] == "error":
            self.hightlight_fields(responce["detail"])
            for i in responce["detail"]:
                values += i["name"] + "\n"
            CTkMessagebox(master=self.tab, icon="cancel", message=values, title="ERROR")
        else:
            CTkMessagebox(master=self.tab, title="SUCESS", message="Материал создан успешно")