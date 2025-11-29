import customtkinter as ctk
from customtkinter import CTk, CTkTabview, CTkButton, CTkEntry, CTkLabel
from CTkTable import CTkTable
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

        self.set_tab2()
        self.set_tab4()

    #ПРИМЕР ЛОГИКИ, УБЕРИ ЕГО ОТ СЕДА
    def ChangingTable_next(self):  # В логику закинешь, это так наработка для тебя
        self.vvalue = [
            [1, "Медь", "500/25", "10 мм²", "Красный", "Сухое помещение", "В наличии", 150],
            [2, "Алюминий", "300/15", "16 мм²", "Серый", "Склад", "На заказ", 0],
            [3, "Сталь", "400/20", "25 мм²", "Оцинкованный", "Цех", "В наличии", 75],
            [4, "ПВХ", "200/10", "6 мм²", "Белый", "Склад", "В наличии", 200],
            [5, "Латунь", "350/18", "12 мм²", "Желтый", "Сухое помещение", "Мало", 10],
            [6, "Бронза", "450/22", "35 мм²", "Золотистый", "Цех", "В наличии", 45]
        ]
        """Обновление данных в таблице"""
        # Предположим, что self.c - это индекс строки для обновления
        self.c = 1  # номер строки в таблице (начиная с 0)
        self.r = 3

        self.new_row_data = self.vvalue[self.c + self.r - 1]  # новые данные для строки
        self.new_row_data_1 = self.vvalue[self.c + self.r]
        self.new_row_data_2 = self.vvalue[self.c + self.r + 1]

        for self.col_index, self.val in enumerate(self.new_row_data):
            self.table.insert(row=self.c, column=self.col_index, value=self.val)
        for self.col_index, self.val in enumerate(self.new_row_data_1):
            self.table.insert(row=self.c + 1, column=self.col_index, value=self.val)
        for self.col_index, self.val in enumerate(self.new_row_data_2):
            self.table.insert(row=self.c + 2, column=self.col_index, value=self.val)
        print(f"Таблица обновлена")

    def ChangingTable_back(self):  # В логику закинешь, это так наработка для тебя
        self.vvalue = [
            [1, "Медь", "500/25", "10 мм²", "Красный", "Сухое помещение", "В наличии", 150],
            [2, "Алюминий", "300/15", "16 мм²", "Серый", "Склад", "На заказ", 0],
            [3, "Сталь", "400/20", "25 мм²", "Оцинкованный", "Цех", "В наличии", 75],
            [4, "ПВХ", "200/10", "6 мм²", "Белый", "Склад", "В наличии", 200],
            [5, "Латунь", "350/18", "12 мм²", "Желтый", "Сухое помещение", "Мало", 10],
            [6, "Бронза", "450/22", "35 мм²", "Золотистый", "Цех", "В наличии", 45]
        ]
        """Обновление данных в таблице"""
        # Предположим, что self.c - это индекс строки для обновления
        self.c = 1  # номер строки в таблице (начиная с 0)
        self.r = 3

        self.new_row_data = self.vvalue[self.c - 1]  # новые данные для строки
        self.new_row_data_1 = self.vvalue[self.c]
        self.new_row_data_2 = self.vvalue[self.r - 1]

        for self.col_index, self.val in enumerate(self.new_row_data):
            self.table.insert(row=self.c, column=self.col_index, value=self.val)
        for self.col_index, self.val in enumerate(self.new_row_data_1):
            self.table.insert(row=self.c + 1, column=self.col_index, value=self.val)
        for self.col_index, self.val in enumerate(self.new_row_data_2):
            self.table.insert(row=self.c + 2, column=self.col_index, value=self.val)
        print(f"Таблица обновлена")

    def set_tab2(self):
        self.value = [
            ["ID", "Материал", "Размер", "Сечение", "Цвет", "Усл.Хранения", "Статус",
             "Ост."],
            [1, "Медь", "500/25", "10 мм²", "Красный", "Сухое помещение", "В наличии", 150],
            [2, "Алюминий", "300/15", "16 мм²", "Серый", "Склад", "На заказ", 0],
            [3, "Сталь", "400/20", "25 мм²", "Оцинкованный", "Цех", "В наличии", 75]
        ]
        self.table = CTkTable(master=self.tab2, values=self.value)
        self.table.pack(expand=True, fill="both", padx=20, pady=20)

        self.tab2_button_1 = CTkButton(self.tab2, width=1, text=">", command=self.ChangingTable_next) #Вперёд
        self.tab2_button_1.place(y=105, x=590)
        self.tab2_button_2 = CTkButton(self.tab2, width=1, text="<", command=self.ChangingTable_back) #Назад
        self.tab2_button_2.place(y=105, x=-1)

    def set_tab4(self):
        self.tab4_label = CTkLabel(self.tab4, text = "Для начала работы перетащите файл в папку 'Data' или же создаёте пустой шаблон")
        self.tab4_label.pack(pady=5)
        self.tab4_button_1 = CTkButton(self.tab4, text = "Закрыть")
        self.tab4_button_1.place(y=35, x=125)
        self.tab4_button_2 = CTkButton(self.tab4, text="Создать шаблон")
        self.tab4_button_2.place(y=35, x=320)
