import tkinter as tk
from tkinter import ttk
from src.SQL_requests import SQLRequests

LOGIN = ''
PASSWORD = ''

COLOR_1 = '#022F40'
COLOR_2 = '#046E8F'


class MainScreen(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.connector = None
        self.login_screen_initial()

    def login_screen_initial(self):
        root.title('login')
        root.geometry('400x200+300+200')

        fields_frame = tk.Frame(root, bg=COLOR_1)
        fields_frame.pack(expand=True)

        login_label = tk.Label(fields_frame, text='Login', bg=COLOR_1, foreground='#fff')
        password_label = tk.Label(fields_frame, text='Password', bg=COLOR_1, foreground='#fff')

        self.login_field = tk.Entry(fields_frame, width=50)
        self.password_field = tk.Entry(fields_frame, width=50)

        login_label.pack()
        self.login_field.pack(ipady=3)
        password_label.pack()
        self.password_field.pack(pady=10, ipady=3)

        agree_btn = tk.Button(fields_frame, text='OK', background=COLOR_2, borderwidth=0, width=25, command=self.sign_in_db)
        agree_btn.bind('<Button-1>')
        agree_btn.pack(ipady=3)

    def sign_in_db(self):

        self.connector = SQLRequests(
            self.login_field.get(),
            self.password_field.get(),
            'lessons',
        )


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.configure(bg=COLOR_1)
    main = MainScreen(root)
    main.mainloop()
