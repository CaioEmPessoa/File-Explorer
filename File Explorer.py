import customtkinter as ctk
import tkinter as tk
import os

class FilesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, app, **kwargs):
        super().__init__(master, **kwargs)

        # Reset / create all
        self.pastas = []
        self.linha = 0
      
        self.numero_pastas = len(self.pastas)

        for self.file in app.files_list:
            if os.path.isdir(self.file):
                self.botao = ctk.CTkButton(master=self, text=self.file ,command=lambda p=self.file: app.check_files(p))
                self.botao.grid(row=self.linha, column=0, pady=3, sticky="w")

                self.linha += 1
            else:
                self.botao = ctk.CTkButton(master=self, text=self.file, fg_color='purple', command=lambda: print("lol"))
                self.botao.grid(row=self.linha, column=0, pady=3, sticky="w")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure Main Window

        # Modes: system (default), light, dark
        ctk.set_appearance_mode("Dark")

        # Themes: blue (default), dark-blue, green
        ctk.set_default_color_theme("blue")

        self.title('Janela')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.minsize(900, 600)
        
        self.check_files('C:')

        # Create Objets
        #entry
        entry = ctk.CTkEntry(master=self, width=300, placeholder_text='Type the dir...')
        entry.grid(pady= 10,
                   row=1, 
                   column=0, 
                   columnspan=2)

        # Send entry to checkfiles
        send = ctk.CTkButton(master=self, text='Send', command=lambda: self.check_files(entry.get()))
        send.grid(row=1, column=2)


    def check_files(self, location):
        self.files_list = []
        print(os.listdir(location))
        for file in os.listdir(location):
            self.file_path = f"{location}\\{file}"
            self.files_list.append(self.file_path)
        print('checado haha')

        self.file_scrobles = FilesFrame(master=self, width=800, height=500, app=self)
        self.file_scrobles.grid(row=0, column=0, columnspan=3 , padx=20)

if __name__ == "__main__":
    root = App()
    root.mainloop()