import streamlit as st


# 웹앱 제목
st.title("스트림릿 테스트")


# 간단한 텍스트 출력
st.write("안녕하세요! Streamlit 앱이 정상적으로 실행되고 있습니다 😃")


# 입력 박스
name = st.text_input("이름을 입력하세요:")


# 버튼
if st.button("확인"):
    st.success(f"환영합니다, {name}님!")
