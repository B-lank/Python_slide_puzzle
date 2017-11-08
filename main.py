from tkinter import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_BACKGROUND = '#f9e9ff'


class Intro:
    def __init__(self):
        self.root = Tk()
        self.set_window()

        self.difficulty = 3
        self.str_difficulty = StringVar()
        self.str_difficulty.set("difficulty : " + format(self.difficulty))

        self.create_widgets()
        self.root.mainloop()

    def set_window(self):
        self.root.title("Slide Puzzle")
        self.root.geometry('{0}x{1}+100+100'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.root.configure(bg=WINDOW_BACKGROUND)
        self.root.resizable(False, False)

    def create_widgets(self):
        self.frame_logo = Frame(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=WINDOW_BACKGROUND)
        self.frame_option = Frame(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=WINDOW_BACKGROUND)
        self.frame_bottom = Frame(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=WINDOW_BACKGROUND)
        self.frame_logo.pack()
        self.frame_option.pack()
        self.frame_bottom.pack()

        self.image_logo = PhotoImage(file="game_logo.png")
        self.label_logo = Label(self.frame_logo, image=self.image_logo, relief=SOLID)
        self.label_logo.image = self.image_logo
        self.label_logo.pack(padx=20, pady=50)

        self.frame_login = Frame(self.frame_option, bg=WINDOW_BACKGROUND)
        self.frame_login.pack(pady=10)
        self.frame_difficulty = Frame(self.frame_option, bg=WINDOW_BACKGROUND)
        self.frame_difficulty.pack(pady=10)

        self.frame_login_input = Frame(self.frame_login, bg=WINDOW_BACKGROUND)
        self.frame_login_input.grid(column=0, row=0)
        self.frame_login_button = Frame(self.frame_login, bg=WINDOW_BACKGROUND, padx=20)
        self.frame_login_button.grid(column=1, row=0)

        self.label_id = Label(self.frame_login_input, text="ID : ", font=("D2Coding", 10), anchor=E, width=15, bg=WINDOW_BACKGROUND)
        self.label_id.grid(column=0, row=0)
        self.label_password = Label(self.frame_login_input, text="PASSWORD : ", font=("D2Coding", 10), anchor=E, width=15, bg=WINDOW_BACKGROUND)
        self.label_password.grid(column=0, row=1)

        self.entry_id = Entry(self.frame_login_input, justify=CENTER)
        self.entry_id.grid(column=1, row=0)
        self.entry_password = Entry(self.frame_login_input, justify=CENTER, show='*')
        self.entry_password.grid(column=1, row=1)

        self.button_register = Button(self.frame_login_button, text='register', width=8, height=1, command=self.register)
        self.button_register.grid(column=0, row=0)
        self.button_login = Button(self.frame_login_button, text='login', width=8, height=1, command=self.login)
        self.button_login.grid(column=0, row=1)

        self.button_minus = Button(self.frame_difficulty, text='<', width=2, height=2, command=self.difficulty_minus)
        self.button_minus.grid(column=0, row=0)
        self.label_difficulty = Label(self.frame_difficulty, textvariable=self.str_difficulty, width=20, height=1, font=("D2Coding", 20), bg=WINDOW_BACKGROUND, relief=SOLID)
        self.label_difficulty.grid(column=1, row=0)
        self.button_plus = Button(self.frame_difficulty, text='>', width=2, height=2, command=self.difficulty_plus)
        self.button_plus.grid(column=2, row=0)

        self.button_start = Button(self.frame_bottom, text='start', width=8, height=2, font=("D2Coding", 20), command=self.game_start)
        self.button_start.pack(pady=20)

    def login(self):
        if len(self.entry_id.get()) < 3:
            self.str_error = "ID have to get more than 3 length"
            print(self.str_error)
            return 0
        if len(self.entry_password.get()) < 6:
            self.str_error = "Password have to get more than 6 length"
            print(self.str_error)
            return 0
        self.user_id = self.entry_id.get()
        self.user_password = self.entry_password.get()
        if self.check_user():
            self.entry_id.delete(0, END)
            self.entry_password.delete(0, END)
            print("Login Success")
        else:
            print("Login Fail")

    def check_user(self):
        with open('user.txt', mode='rt', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line: break
                if line.split('$')[0] == self.user_id:
                    if line.split('$')[1] == self.user_password:
                        return True
            return False

    def difficulty_plus(self):
        if 3 <= self.difficulty < 5:
            self.difficulty += 1
            self.str_difficulty.set("difficulty : " + format(self.difficulty))

    def difficulty_minus(self):
        if 3 < self.difficulty <= 5:
            self.difficulty -= 1
            self.str_difficulty.set("difficulty : " + format(self.difficulty))

    def register(self):
        window_register = Register()

    def game_start(self):
        self.root.destroy()
        window_game = Game(self.difficulty)


class Register:
    def __init__(self):
        self.root = Tk()

        self.set_window()
        self.create_widgets()

        self.root.mainloop()

    def set_window(self):
        self.root.title("Register")
        self.root.geometry('400x90+300+400')
        self.root.configure(bg=WINDOW_BACKGROUND)
        self.root.resizable(False, False)

    def create_widgets(self):
        self.frame_login = Frame(self.root, bg=WINDOW_BACKGROUND)
        self.frame_login.grid(column=0, row=0)
        self.frame_login_input = Frame(self.frame_login, width=200, pady=10, bg=WINDOW_BACKGROUND)
        self.frame_login_input.grid(column=0, row=0)
        self.frame_login_button = Frame(self.frame_login, width=180, padx=20, bg=WINDOW_BACKGROUND)
        self.frame_login_button.grid(column=1, row=0)

        self.label_id = Label(self.frame_login_input, text="ID : ", font=("D2Coding", 10), anchor=E, width=15, bg=WINDOW_BACKGROUND)
        self.label_id.grid(column=0, row=0)
        self.label_password = Label(self.frame_login_input, text="PASSWORD : ", font=("D2Coding", 10), anchor=E, width=15, bg=WINDOW_BACKGROUND)
        self.label_password.grid(column=0, row=1)

        self.entry_id = Entry(self.frame_login_input, justify=CENTER)
        self.entry_id.grid(column=1, row=0)
        self.entry_password = Entry(self.frame_login_input, justify=CENTER)
        self.entry_password.grid(column=1, row=1)

        self.button_check = Button(self.frame_login_button, text='check', width=8, height=1, command=self.check)
        self.button_check.grid(column=0, row=0)
        self.button_register = Button(self.frame_login_button, text='register', width=8, height=1, command=self.register, state='disabled')
        self.button_register.grid(column=0, row=1)

        self.str_error = StringVar()
        self.label_error = Label(self.root, width=40, height=1, textvariable=self.str_error, justify=CENTER, fg='red', bg=WINDOW_BACKGROUND)
        self.str_error.set("hello")
        self.label_error.grid(column=0, row=1)

    def check_user(self):
        with open('user.txt', mode='rt', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line: break
                if line.split('$')[0] == self.user_id:
                    return True

    def check(self):
        if len(self.entry_id.get()) < 3:
            self.str_error.set("ID have to get more than 3 length")
            return 0
        if len(self.entry_password.get()) < 6:
            self.str_error.set("Password have to get more than 6 length")
            return 0
        self.user_id = self.entry_id.get()
        self.user_password = self.entry_password.get()
        if not self.check_user():
            self.check = True
            self.entry_id.config(state='disabled')
            self.entry_password.config(state='disabled')
            self.button_register.config(state='normal')
            self.str_error.set("Click register button")
        else:
            self.check = False
            self.str_error.set("Register Fail")

    def register(self):
        if self.check:
            with open('user.txt', mode='at', encoding='utf-8') as file:
                file.write("\n%s$%s" % (self.user_id, self.user_password))
            self.root.destroy()


class Game:
    def __init__(self, difficulty):
        self.root = Tk()

        self.set_window()

        self.difficulty = difficulty
        self.a = Label(self.root, text=self.difficulty, font=("D2Coding", 50))
        self.a.pack()

        self.root.mainloop()

    def set_window(self):
        self.root.title("Slide Puzzle")
        self.root.geometry('1366x768+100+100')
        self.root.configure(bg='white')
        self.root.resizable(False, False)


if __name__ == "__main__":
    window_intro = Intro()
