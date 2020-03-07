import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from src.SQL_requests import SQLRequests
import mysql.connector

LOGIN = ''
PASSWORD = ''

COLOR_1 = '#2e5266'
COLOR_2 = '#d3d0cb'
COLOR_3 = '#6e8898'
COLOR_4 = '#9fb1bc'
COLOR_5 = '#e2c044'


class MainScreen(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.connector = None
        self.login_screen_initial()
        self.table = None

    def login_screen_initial(self):
        root.title('login')
        root.geometry('400x200+300+200')

        fields_frame = tk.Frame(root, bg=COLOR_1)
        fields_frame.pack(expand=True)

        login_label = tk.Label(fields_frame, text='Login', bg=COLOR_1, foreground='#fff')
        password_label = tk.Label(fields_frame, text='Password', bg=COLOR_1, foreground='#fff')

        login_field = tk.Entry(fields_frame, width=50)
        password_field = tk.Entry(fields_frame, width=50)

        login_label.pack(pady=10)
        login_field.pack(ipady=3)
        password_label.pack(pady=10)
        password_field.pack(ipady=3)

        agree_btn = tk.Button(
            fields_frame, text='OK',
            background=COLOR_2,
            borderwidth=0, width=25,
        )
        agree_btn.bind('<Button-1>', lambda sign_in_db: self.sign_in_db(login_field, password_field, fields_frame))
        agree_btn.pack(ipady=3, pady=20)

    def sign_in_db(self, login_field, password_field, fields_frame):
        try:
            self.connector = SQLRequests(
                login_field.get(),
                password_field.get(),
                'lessons',
            )
        except mysql.connector.errors.ProgrammingError:
            raise messagebox.showerror('Error', 'Un correct password or username')

        fields_frame.destroy()
        self.main_screen()

    def main_screen(self):
        root.geometry('700x400+400+300')

        response = self.connector.get(
            'person',
            fields='*'
        )

        # TABLE ==================================================================//
        self.table = ttk.Treeview(root, columns=('id', 'name', 'age'), height=15, show='headings')

        self.table.column('id', width=50, anchor='center')
        self.table.column('name', width=100, anchor='center')
        self.table.column('age', width=70, anchor='center')

        self.table.heading('id', text='ID')
        self.table.heading('name', text='Name')
        self.table.heading('age', text='Age')

        self.table.pack(sid='top')

        for num, i in enumerate(response, 1):
            self.table.insert('', num, value=i)

        # BOTTOM MENU ============================================================//
        bottom_menu = tk.Frame(root, borderwidth=0, bg=COLOR_3)
        bottom_menu.pack(side='bottom')

        btn_add = tk.Button(bottom_menu, bg=COLOR_5, text='Add', fg=COLOR_1,  borderwidth=0)
        btn_remove = tk.Button(bottom_menu, bg=COLOR_5, text='Remove', fg=COLOR_1,  borderwidth=0)
        btn_change = tk.Button(bottom_menu, bg=COLOR_5, text='Change', fg=COLOR_1,  borderwidth=0)

        btn_add.grid(column=0, row=1, pady=20, padx=80, ipadx=15, ipady=10)
        btn_remove.grid(column=1, row=1, pady=20, padx=80, ipadx=15, ipady=10)
        btn_change.grid(column=2, row=1, pady=20, padx=80, ipadx=15, ipady=10)


class SecondScreen(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.resizable(False, False)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.configure(bg=COLOR_1)
    main = MainScreen(root)
    main.mainloop()
