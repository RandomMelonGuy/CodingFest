import customtkinter as ctk
from customtkinter import CTk, CTkTabview, CTkButton, CTkEntry, CTkLabel
from CTkTable import CTkTable
from .tabs.AddTab import AddTab
from .tabs.browseTab import BrowseTab
from .tabs.RepelishTab import RepelishTab

class TestView(CTk):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.geometry(f'665x340+{(self.winfo_screenwidth() - 665) // 2}+{(self.winfo_screenheight() - 340) // 2}')
        self.minsize(665, 340)
        self.maxsize(665, 340)
        self.curIndex = 0
        self.per_page = 3
        self.tabview = CTkTabview(self, command=self.on_switch)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)
        self.tab1 = self.tabview.add("Добавить материал")
        self.tab2 = self.tabview.add("Просмотр и фильтрация")
        self.tab3 = self.tabview.add("Списание/пополнение")
        self.tab4 = self.tabview.add("Загрузка данных")

        self.addTab = AddTab(self.tab1, self.presenter)
        self.repTab = RepelishTab(master=self.tab3, presenter=self.presenter)
        self.browseTab = BrowseTab(master=self.tab2, presenter=self.presenter)
        self.set_tab4()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_switch(self):
        if self.tabview.get() == "Списание/пополнение":
            self.repTab.update_combo()

    def on_closing(self):
        self.presenter.save()
        self.destroy()

    def set_tab4(self):
        self.tab4_label = CTkLabel(self.tab4, text = "Для начала работы перетащите файл в папку 'Data' или же создаёте пустой шаблон")
        self.tab4_label.pack(pady=5)
        self.tab4_button_1 = CTkButton(self.tab4, text = "Закрыть")
        self.tab4_button_1.place(y=35, x=125)
        self.tab4_button_2 = CTkButton(self.tab4, text="Создать шаблон")
        self.tab4_button_2.place(y=35, x=320)
