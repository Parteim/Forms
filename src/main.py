import tkinter as tk
from tkinter import ttk
import mysql.connector as mycon

COLOR_1 = '#022F40'
COLOR_2 = '#046E8F'


class MainScreen(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.login_screen_initial()

    def login_screen_initial(self):
        root.title('login')
        root.geometry('400x200+300+200')

        fields_frame = tk.Frame(root, bg=COLOR_1)
        fields_frame.pack(expand=True)

        login_field = tk.Entry(fields_frame, width=50)
        password_field = tk.Entry(fields_frame, width=50)

        login_field.pack(ipady=3)
        password_field.pack(pady=10, ipady=3)

        agree_btn = tk.Button(fields_frame, text='OK', background=COLOR_2, borderwidth=0, width=25)
        agree_btn.bind('<Button-1>')
        agree_btn.pack(ipady=3)


def _main():
    conn = mycon.connection.MySQLConnection(
        user='root', password='1234',
        host='127.0.0.1',
        database='lessons'
    )

    curs = conn.cursor(buffered=True)

    curs.execute(
        """
        SELECT * 
        FROM person
        """
    )

    for row in curs:
        print(row)


if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(False, False)
    root.configure(bg=COLOR_1)
    main = MainScreen(root)
    main.mainloop()
