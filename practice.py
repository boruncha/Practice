from Config import host, user, password, db_name
import tkinter as tk
import ttkbootstrap as ttk
import pymysql

connection = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    database=db_name
)
cur = connection.cursor()



class PracApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Практика")
        self.geometry("600x600")
        self.resizable(False, False)
        self.putpassword()

    def putpassword(self):
        self.startlab = ttk.Label(text="Требуется вход в учетную запись", font=("Helvetica", 24, 'bold'))
        self.startlab.pack(pady=20)
        self.loginlab = ttk.Label(text="Введите логин", font=("Helvetica", 20))
        self.loginlab.pack(pady=20)
        self.entrylogin = ttk.Entry(self)
        self.entrylogin.pack(pady=20)
        self.passwordlab = ttk.Label(text="Введите пароль", font=("Helvetica", 20))
        self.passwordlab.pack(pady=20)
        self.entrypassword = ttk.Entry(self, show="*")
        self.entrypassword.pack(pady=20)
        self.logbutton = ttk.Button(text="Войти в приложение", command=self.log)
        self.logbutton.pack(pady=10)
        self.alarmlab = ttk.Label(text="", font=("Helvetica", 20), foreground="red")
        self.alarmlab.pack(pady=20)

    def log(self):
        cur.execute("select * from users where login=%s and password=%s",
                    (self.entrylogin.get(), self.entrypassword.get()))
        row = cur.fetchone()
        if row == None:
            self.alarmlab.config(text="В доступе отказано")
        else:
            self.logdes()
            self.standput()

    def logdes(self):
        self.startlab.destroy()
        self.loginlab.destroy()
        self.entrylogin.destroy()
        self.passwordlab.destroy()
        self.entrypassword.destroy()
        self.logbutton.destroy()
        self.alarmlab.destroy()

    def standdes(self):
        self.tree.destroy()
        columns = ('ID', 'IP', 'Date')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.column("ID", anchor=tk.CENTER)
        self.tree.column("IP", anchor=tk.CENTER)
        self.tree.column("Date", anchor=tk.CENTER)
        self.tree.place(relx=0, rely=0)
        for c in columns:
            self.tree.heading(c, text=c)

        cur.execute("select ID, IP, IP_date from apache_log")
        values = cur.fetchall()

        for value in values:
            self.tree.insert('', tk.END, values=value)

        self.scrlb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrlb.place(relx=0.978, rely=0.175, relheight=0.3, relwidth=0.02, y=-100)
        self.tree.configure(yscrollcommand=self.scrlb.set)
        self.sortl.config(text="(Стандартная сортировка)")
        self.sortl.place(x=100, y=250)

    def datades(self):
        self.tree.destroy()
        columns = ('ID', 'IP', 'Date')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.column("ID", anchor=tk.CENTER)
        self.tree.column("IP", anchor=tk.CENTER)
        self.tree.column("Date", anchor=tk.CENTER)
        self.tree.place(relx=0, rely=0)
        for c in columns:
            self.tree.heading(c, text=c)

        cur.execute(f"select ID, IP, IP_date from apache_log where Ip_date = '{self.datasortentry.get()}'")
        values = cur.fetchall()

        for value in values:
            self.tree.insert('', tk.END, values=value)

        self.scrlb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrlb.place(relx=0.978, rely=0.175, relheight=0.3, relwidth=0.02, y=-100)
        self.tree.configure(yscrollcommand=self.scrlb.set)
        self.sortl.config(text=f"(Фильтрация по дате {self.datasortentry.get()})")
        self.sortl.place(x=40, y=250)

    def ipdes(self):
        self.tree.destroy()
        columns = ('ID', 'IP', 'Date')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.column("ID", anchor=tk.CENTER)
        self.tree.column("IP", anchor=tk.CENTER)
        self.tree.column("Date", anchor=tk.CENTER)
        self.tree.place(relx=0, rely=0)
        for c in columns:
            self.tree.heading(c, text=c)

        cur.execute(f"select ID, IP, IP_date from apache_log where ip = '{self.ipsortentry.get()}'")
        values = cur.fetchall()

        for value in values:
            self.tree.insert('', tk.END, values=value)

        self.scrlb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrlb.place(relx=0.978, rely=0.175, relheight=0.3, relwidth=0.02, y=-100)
        self.tree.configure(yscrollcommand=self.scrlb.set)
        self.sortl.config(text=f"(Фильтрация по айпи {self.ipsortentry.get()})")
        self.sortl.place(x=30, y=250)

    def standput(self):
        columns = ('ID', 'IP', 'Date')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        self.tree.column("ID", anchor=tk.CENTER)
        self.tree.column("IP", anchor=tk.CENTER)
        self.tree.column("Date", anchor=tk.CENTER)
        self.tree.place(relx=0, rely=0)
        for c in columns:
            self.tree.heading(c, text=c)

        cur.execute("select ID, IP, IP_date from apache_log")
        values = cur.fetchall()

        for value in values:
            self.tree.insert('', tk.END, values=value)

        self.scrlb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.scrlb.place(relx=0.978, rely=0.175, relheight=0.3, relwidth=0.02, y=-100)
        self.tree.configure(yscrollcommand=self.scrlb.set)
        self.welc = ttk.Label(text="Добро пожаловать",  font=("Helvetica", 24, 'bold'))
        self.sortl = ttk.Label(text="(Стандартная сортировка)", font=("Helvetica", 24, 'bold'))
        self.welc.place(x=150, y=200)
        self.sortl.place(x=100, y=250)
        self.standsortbut = ttk.Button(text="Стандартная сортировка", command=self.standdes)
        self.standsortbut.place(x=20, y=325)
        self.datasortbut = ttk.Button(text="Фильтрация по дате", command=self.datades)
        self.datasortbut.place(x=240, y=325)
        self.datasortl = ttk.Label(text="Дата в формате YYYY/MM/DD", font=("Helvetica", 12))
        self.datasortl.place(x=200, y=360)
        self.datasortentry = ttk.Entry()
        self.datasortentry.place(x=240, y=400)
        self.ipsortbut = ttk.Button(text="Фильтрация по айпи", command=self.ipdes)
        self.ipsortbut.place(x=445, y=325)
        self.ipsortentry = ttk.Entry()
        self.ipsortentry.place(x=445, y=400)



Pracapp = PracApp()
Pracapp.mainloop()
