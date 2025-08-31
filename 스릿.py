import streamlit as st
import datetime

# 제목
st.title("✨ 나만의 스트림릿 웹앱 ✨")

# 오늘 날짜 표시
st.write("📅 오늘 날짜:", datetime.date.today())

# 슬라이더 (숫자 입력)
age = st.slider("나이를 선택하세요", min_value=10, max_value=30, value=17)

# 이름 입력
name = st.text_input("이름을 입력하세요:")

# 학교 입력
school = st.text_input("학교를 입력하세요:")

# 학년, 반, 번호 입력
grade = st.number_input("학년을 입력하세요:", min_value=1, max_value=6, step=1)
class_num = st.number_input("반을 입력하세요:", min_value=1, max_value=10, step=1)
student_num = st.number_input("번호를 입력하세요:", min_value=1, max_value=50, step=1)

# 버튼
if st.button("확인하기"):
    st.success(
        f"환영합니다 {name}님! 🎉\n"
        f"나이: {age}살\n"
        f"학교: {school}\n"
        f"{grade}학년 {class_num}반 {student_num}번"
    )
