from customtkinter import CTkFrame, CTkLabel, CTkButton
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog

class ExportTab(CTkFrame):
    def __init__(self, master, presenter):
        self.master = master
        self.presenter = presenter
        self.setupUI()

    def setupUI(self):
        self.tab4_label = CTkLabel(self.master, text = "Для экспорта данных для начала выберите путь для сохранения")
        self.tab4_label.pack(pady=5)
        self.tab4_button_2 = CTkButton(self.master, text="Экспортировать в файл", command=self.export_file)
        self.tab4_button_2.place(y=35, x=320)
    
    def export_file(self):
        filepath = filedialog.asksaveasfilename(filetypes=[("Excel table", "*.xlsx")], title="Сохранить копию данных")
        if filepath:
            responce = self.presenter.export_file(filepath)
            if responce:
                CTkMessagebox(master=self.master, title="INFO", message="Файл экспортирован успешно", icon="check")
            else:
                CTkMessagebox(master=self.master, title="ERROR", message="Ошибка при экспорте файла", icon="cancel")
