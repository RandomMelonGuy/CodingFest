import customtkinter as ctk
from customtkinter import CTk, CTkTabview, CTkButton, CTkEntry, CTkLabel
from CTkTable import CTkTable
from .tabs.AddTab import AddTab
from .tabs.browseTab import BrowseTab
from .tabs.RepelishTab import RepelishTab
from .tabs.ExportTab import ExportTab

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
        self.tab4 = self.tabview.add("Экспорт данных данных")

        self.addTab = AddTab(self.tab1, self.presenter)
        self.repTab = RepelishTab(master=self.tab3, presenter=self.presenter)
        self.browseTab = BrowseTab(master=self.tab2, presenter=self.presenter)
        self.exportTab = ExportTab(master=self.tab4, presenter=presenter)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_switch(self):
        if self.tabview.get() == "Списание/пополнение":
            self.repTab.update_combo()
        elif self.tabview.get() == "Просмотр и фильтрация":
            self.browseTab.setupData()

    def on_closing(self):
        self.presenter.save()
        self.destroy()
