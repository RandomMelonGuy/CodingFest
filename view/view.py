from customtkinter import CTk, CTkTabview, CTkButton, CTkEntry, CTkLabel
from .tabs.AddTab import AddTab

class TestView(CTk):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.geometry(f'665x340+{(self.winfo_screenwidth() - 665) // 2}+{(self.winfo_screenheight() - 340) // 2}')
        self.minsize(665, 340)
        self.maxsize(665, 340)
        self.tabview = CTkTabview(self)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)

        self.tab1 = self.tabview.add("Добавить материал")
        self.tab2 = self.tabview.add("Просмотр и фильтрация")
        self.tab3 = self.tabview.add("Списание/пополнение")
        self.tab4 = self.tabview.add("Загрузка данных")

        AddTab(self.tab1, self.presenter)

        self.set_tab4()

    def set_tab4(self):
        self.tab4_label = CTkLabel(self.tab4, text = "Для начала работы перетащите файл в папку 'Data' или же создаёте пустой шаблон")
        self.tab4_label.pack(pady=5)
        self.tab4_button_1 = CTkButton(self.tab4, text = "Закрыть")
        self.tab4_button_1.place(y=35, x=125)
        self.tab4_button_2 = CTkButton(self.tab4, text="Создать шаблон")
        self.tab4_button_2.place(y=35, x=320)
