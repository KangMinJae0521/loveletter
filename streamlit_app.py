import streamlit as st

def main():
    # 앱의 타이틀 설정
    st.title("연애 조언 앱")

    # 사용자의 말을 표시
    st.write('나: "하...연애하고 싶다."')

    # '연애 조언 받기' 버튼 생성
    if st.button("연애 조언 받기"):
        # 버튼을 클릭했을 때 표시될 메시지
        st.write("조언: 자신감을 가지세요! 누군가는 당신의 매력에 반할 거예요.")

# 스트림릿 앱을 실행
if __name__ == "__main__":
    main()
