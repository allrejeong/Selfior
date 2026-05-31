import streamlit as st

st.title("🌱 Selfior - 나를 구하는 하루")
energy = st.slider("오늘의 에너지 점수 (1-10)", 1, 10, 5)

todo_list = ["수학 쎈 C단계 3문제", "영어 단어 50개", "운동 30분", "일기 쓰기"]

if energy <= 3:
    st.warning("오늘은 회복이 우선이에요! 이것만 해요.")
    final_todo = [todo_list[3]]
elif energy <= 7:
    st.info("평소대로 차근차근 해볼까요?")
    final_todo = todo_list
else:
    st.success("에너지가 좋네요! 추가 도전도 추천해요.")
    final_todo = todo_list + ["독서 30분"]

for item in final_todo:
    st.checkbox(item)
