import streamlit as st
import time

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
        if "advice_requested" not in st.session_state:
            st.session_state.advice_requested = False
        if "dialogue_shown" not in st.session_state:
            st.session_state.dialogue_shown = False

        if st.session_state.dialogue_shown == False:
            # 대사 표시
            st.write('나: "하...연애하고 싶다...ㅠㅠ"')
            time.sleep(3)
            st.write('나: "누가 연애 조언 안해주나...?"')
            time.sleep(3)
            st.write('슝슝이: "안녕? 난 슝슝이야!"')
            time.sleep(3)
            st.write('슝슝이: "내가 너의 모솔 탈출을 도와줄게!"')
            time.sleep(3)
            st.write('슝슝이: "일단 내가 만든 질문에 답을 해봐!"')
            time.sleep(3)
            st.session_state.dialogue_shown = True

        if st.button("연애 조언 받기"):
            st.session_state.advice_requested = True

        if st.session_state.advice_requested:
            for info_type, options in self.options.items():
                choice = st.radio(f"당신의 {info_type}을 선택하세요:", options)
                self.set_user_info(info_type, choice)

            if st.button("조언 받기"):
                self.show_advice()

            if st.button("초기화"):
                self.user_info = {}
                st.session_state.advice_requested = False
                st.session_state.dialogue_shown = False
                st.experimental_rerun()

def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.banggooso.com/assets/images/uploadImg/1596642366(M).jpg");
            background-size: 50%;
            background-position: center top;
          
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    add_bg_from_local()
    
    # 앱의 타이틀 설정
    st.title("사랑을 찾아 슝슝~♥")

    # 연애 조언 앱 실행
    app = LoveAdviceApp()
    app.run()

if __name__ == "__main__":
    main()
