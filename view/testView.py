from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel


class TestView(CTk):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.label = CTkLabel(self)
        self.entry = CTkEntry(self)
        self.button = CTkButton(self, command=self.sendData)
        self.entry.pack()
        self.label.pack()
        self.button.pack()

    def sendData(self):
        # need data -> send request -> get responce -> update data
        maxVal = int(self.entry.get())
        responce = self.presenter.get_random(maxVal)
        self.label.configure(text=responce)
