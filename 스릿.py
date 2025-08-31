import streamlit as st
import datetime


# 제목
st.title("✨ 나만의 스트림릿 웹앱 ✨")


# 오늘 날짜 표시
st.write("📅 오늘 날짜:", datetime.date.today())


# 슬라이더 (숫자 입력)
age = st.slider("나이를 선택하세요", min_value=10, max_value=30, value=17)


# 입력
name = st.text_input("이름을 입력하세요:") 


# 버튼
if st.button("확인하기"):
    st.success(f"환영합니다 {name}님! 당신은 {age}살 이군요 🎉")


# 재미 기능: 풍선 터뜨리기
if st.button("🎈 풍선!"):
    st.balloons()