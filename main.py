from tkinter import *
import createGrid
import ranking

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_BACKGROUND = '#f9e9ff'


class Intro:  # 인트로 클래스
    def __init__(self):
        self.root = Tk()
        self.set_window()  # 창 설정
        self.create_widgets()  # 화면 구성
        self.root.mainloop()

    def set_window(self):  # 창 설정 메소드
        self.root.title("Slide Puzzle")
        self.root.geometry('{0}x{1}+100+100'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.root.configure(bg=WINDOW_BACKGROUND)
        self.root.resizable(False, False)  # 창 크기 변경 불가

    def create_widgets(self):  # 화면 구성 메소드
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

        self.entry_id = Entry(self.frame_login_input, justify=CENTER)  # 아이디 입력 창
        self.entry_id.grid(column=1, row=0)
        self.entry_password = Entry(self.frame_login_input, justify=CENTER, show='*')  # 비밀번호 입력 창
        self.entry_password.grid(column=1, row=1)

        self.button_register = Button(self.frame_login_button, text='register', width=8, height=1, command=self.register)  # 회원가입 버튼 - 새로운 창 띄움
        self.button_register.grid(column=0, row=0)
        self.button_login = Button(self.frame_login_button, text='login', width=8, height=1, command=self.login)  # 로그인 버튼
        self.button_login.grid(column=0, row=1)

        self.difficulty = 3  # 3*3 퍼즐이 기본값
        self.str_difficulty = StringVar()  # 난이도 문자열
        self.str_difficulty.set("difficulty : " + format(self.difficulty))

        self.button_minus = Button(self.frame_difficulty, text='<', width=2, height=2, command=self.difficulty_minus)  # 난이도 감소
        self.button_minus.grid(column=0, row=0)
        self.label_difficulty = Label(self.frame_difficulty, textvariable=self.str_difficulty, width=20, height=1, font=("D2Coding", 20), bg=WINDOW_BACKGROUND, relief=SOLID)
        self.label_difficulty.grid(column=1, row=0)
        self.button_plus = Button(self.frame_difficulty, text='>', width=2, height=2, command=self.difficulty_plus)  # 난이도 증가
        self.button_plus.grid(column=2, row=0)

        self.str_error = StringVar()
        self.label_error = Label(self.frame_bottom, textvariable=self.str_error, width=50, height=1, justify=CENTER, fg='red', bg='white', font=("D2Coding", 9))
        self.label_error.pack(pady=10)
        self.button_start = Button(self.frame_bottom, text='start', width=8, height=2, font=("D2Coding", 20), command=self.game_start, state='disabled')  # 게임 시작 버튼 - 창 없애고 새 창 띄움
        self.button_start.pack(pady=20)

    def login(self):  # 로그인 메소드
        if len(self.entry_id.get()) < 3:  # 아이디는 3자 이상
            self.str_error.set("ID have to get more than 3 length")
            return 0
        if len(self.entry_password.get()) < 6:  # 비밀번호는 6자 이상
            self.str_error.set("Password have to get more than 6 length")
            return 0
        self.user_id = self.entry_id.get()  # 아이디 입력 창에서 받아오기
        self.user_password = self.entry_password.get()  # 비밀번호 입력 창에서 받아오기
        if self.check_user():  # 일치하는 정보가 존재하면
            self.entry_id.configure(state='disabled')  # 아이디 입력 창 비활성화
            self.entry_password.configure(state='disabled')  # 비밀번호 입력 창 비활성화
            self.button_register.configure(state='disabled')  # 회원가입 버튼 비활성화
            self.button_login.configure(state='disabled')  # 로그인 버튼 비활성화
            self.button_start.configure(state='normal')  # 게임 시작 버튼 활성화
            self.rank, self.highest_score = ranking.get_rank(self.user_id)
            self.str_error.set("Rank : %s / Highest score : %s" % (self.rank, self.highest_score))
        else:
            self.str_error.set("Login Fail")

    def check_user(self):  # 일치하는 정보 확인
        with open('user.txt', mode='rt', encoding='utf-8') as file:  # 유저 정보가 들어있는 파일
            while True:
                line = file.readline()
                if not line: break  # 파일 끝이면 종료s
                if line.split('$')[0] == self.user_id:  # 아이디 일치
                    if line.split('$')[1].split('\n')[0] == self.user_password:  # 비밀번호 일치
                        return True
            return False

    def difficulty_plus(self):  # 난이도 증가
        if 3 <= self.difficulty < 5:
            self.difficulty += 1
            self.str_difficulty.set("difficulty : " + format(self.difficulty))

    def difficulty_minus(self):  # 난이도 감소
        if 3 < self.difficulty <= 5:
            self.difficulty -= 1
            self.str_difficulty.set("difficulty : " + format(self.difficulty))

    def register(self):  # 회원가입 메소드
        window_register = Register()  # 회원가입 객체 생성

    def game_start(self):  # 게임 시작 메소드
        self.root.destroy()  # 인트로 창 종료
        window_game = createGrid.mainGrid(self.user_id, self.rank, self.highest_score, self.difficulty)  # 게임 객체 생성


class Register:  # 회원가입 클래스
    def __init__(self):
        self.root = Tk()
        self.set_window()  # 창 설정
        self.create_widgets()  # 화면 구성
        self.root.mainloop()

    def set_window(self):
        self.root.title("Register")
        self.root.geometry('400x90+300+400')
        self.root.configure(bg=WINDOW_BACKGROUND)
        self.root.resizable(False, False)  # 창 크기 변경 불가

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
        self.str_error.set("hello")
        self.label_error = Label(self.root, width=30, height=1, font=("D2Coding", 9), textvariable=self.str_error, justify=CENTER, fg='red', bg='white')
        self.label_error.grid(column=0, row=1)

    def check_user(self):
        with open('user.txt', mode='rt', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if not line: break
                if line.split('$')[0] == self.user_id:
                    return True
            return False

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


if __name__ == "__main__":
    window_intro = Intro()
