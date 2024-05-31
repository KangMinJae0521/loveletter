import streamlit as st

class StartWindow:
    def __init__(self, master):
        self.master = master
        self.setup_ui()

    def setup_ui(self):
        self.master.title("연애 조언 앱 시작")
        self.master.geometry("400x500")  # 초기 창 크기 조정
        self.master.configure(bg='#f0e0d6')  # 초기 창 배경색 변경

        # 버튼 폰트 설정
        button_font = tkfont.Font(family='Helvetica', size=12)

        # 대사
        self.user_says_label = tk.Label(self.master, text='나: "하...연애하고 싶다."', bg='#f7d7e0', fg='#333', font=("Helvetica", 12))
        self.user_says_label.pack(pady=5)
    
        # 대사
        self.user_says_label = tk.Label(self.master, text='나: "누가 나한테 연애 조언 안해주나..?"', bg='#f7d7e0', fg='#333', font=("Helvetica", 12))
        self.user_says_label.pack(pady=5)

        # 대사
        self.user_says_label = tk.Label(self.master, text='슝슝이: "이봐! 모솔인 너! 내가 도와줄게"', bg='#f7d7e0', fg='#333', font=("Helvetica", 12))
        self.user_says_label.pack(pady=5)
        
        # '연애 조언 받기' 버튼
        tk.Button(self.master, text="연애 조언 받기", font=button_font, bg='#ffebcd', fg='#333', command=self.open_love_advice_app).pack(expand=True)

       

    
    def open_love_advice_app(self):
        # 연애 조언 앱 창을 여는 로직
        self.love_advice_window = tk.Toplevel(self.master)  # 기존 창의 자식 창으로 연애 조언 앱 창을 생성
        self.app = LoveAdviceApp(self.love_advice_window)

class LoveAdviceApp:
    def __init__(self, master):
        self.master = master
        self.user_info = {}
        self.setup_ui()

    def setup_ui(self):
        self.master.title("연애 조언 앱")
        self.master.configure(bg='#f7d7e0')  # 배경색 변경
        self.master.geometry("400x200")  # 창 크기 조절
        
        # 타이틀 레이블
        title_font = tkfont.Font(family='Helvetica', size=16, weight="bold")
        self.title_label = tk.Label(self.master, text="당신의 연애 스타일은?", bg='#f7d7e0', fg='#333', font=title_font)
        self.title_label.pack(pady=10)
        
        # 버튼 폰트 설정
        button_font = tkfont.Font(family='Helvetica', size=12)
        
        self.options = {
            "age": ["20대", "30대", "40대 이상"],
            "interest": ["영화", "책", "운동"]
        }
        
        self.buttons = {}
        
        for info_type, options in self.options.items():
            frame = tk.Frame(self.master, bg='#f7d7e0')  # 프레임 배경색 변경
            frame.pack(padx=10, pady=5)
            
            for option in options:
                button = tk.Button(frame, text=option, font=button_font, bg='#fff', fg='#333',
                                   command=lambda option=option, info_type=info_type: self.set_user_info(info_type, option))
                button.pack(side=tk.LEFT, padx=5)
                if info_type not in self.buttons:
                    self.buttons[info_type] = []
                self.buttons[info_type].append(button)
        
        # 조언 받기 버튼
        tk.Button(self.master, text="조언 받기", font=button_font, bg='#ffebcd', fg='#333', command=self.show_advice).pack(pady=5)
        
        # 초기화 버튼
        tk.Button(self.master, text="초기화", font=button_font, bg='#ffebcd', fg='#333', command=self.reset_choices).pack(pady=5)

    def set_user_info(self, info_type, option):
        self.user_info[info_type] = option
        for button in self.buttons[info_type]:
            if button['text'] == option:
                button.config(relief=tk.SUNKEN, bg="#b1a7a6")
            else:
                button.config(relief=tk.RAISED, bg="SystemButtonFace")
                
    def reset_choices(self):
        self.user_info = {}
        for info_type in self.buttons:
            for button in self.buttons[info_type]:
                button.config(relief=tk.RAISED, bg="#fff")
    
    def show_advice(self):
        age = self.user_info.get("age", "미정")
        interest = self.user_info.get("interest", "미정")
        advice = f"당신은 {age}이고, 관심사는 {interest}입니다. 사랑은 언제나 가까이에 있습니다."
        messagebox.showinfo("연애 조언", advice)
        
def main():
    root = tk.Tk()
    app = StartWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
