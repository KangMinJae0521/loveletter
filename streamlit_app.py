import streamlit as st

class LoveAdviceApp:
    def __init__(self):
        self.user_info = {}
        self.options = {
            "age": ["20대", "30대", "40대 이상"],
            "interest": ["영화", "책", "운동"]
        }
    
    def set_user_info(self, info_type, option):
        self.user_info[info_type] = option
    
    def show_advice(self):
        age = self.user_info.get("age", "미정")
        interest = self.user_info.get("interest", "미정")
        advice = f"당신은 {age}이고, 관심사는 {interest}입니다. 사랑은 언제나 가까이에 있습니다."
        st.info(advice)
    
    def run(self):
        st.title("연애 조언 앱")
        
        for info_type, options in self.options.items():
            choice = st.radio(f"당신의 {info_type}을 선택하세요:", options)
            self.set_user_info(info_type, choice)
        
        if st.button("조언 받기"):
            self.show_advice()
        
        if st.button("초기화"):
            self.user_info = {}
            st.experimental_rerun()

if __name__ == "__main__":
    app = LoveAdviceApp()
    app.run()
    root.mainloop()

if __name__ == "__main__":
    main()
