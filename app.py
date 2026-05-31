import streamlit as st

st.title("🌱 Selfior - 나를 구하는 하루")

# 1. 에너지 측정
energy = st.slider("오늘의 에너지 점수 (1-10)", 1, 10, 5)

# 2. 카테고리별 할 일 데이터 (여기에 동생이 하고 싶은 거 다 적으면 돼!)
work_tasks = ["보고서 쓰기", "메일 확인"]
dev_tasks = ["수학 쎈 C단계", "영어 단어 50개"]
life_tasks = ["고양이 화장실 청소", "운동 30분"]

# 3. 에너지에 따른 투두리스트 추출 로직
if energy <= 3:
    st.warning("오늘은 회복이 우선이에요! 딱 한 가지만 할까요?")
    final_todo = [dev_tasks[0]] # 공부 중 하나만!
elif energy <= 7:
    st.info("평소대로 차근차근 해볼까요?")
    final_todo = work_tasks + dev_tasks
else:
    st.success("에너지가 좋네요! 다 해낼 수 있어요!")
    final_todo = work_tasks + dev_tasks + life_tasks

# 4. 결과 보여주기 (체크박스로!)
st.subheader("오늘의 미션")
for item in final_todo:
    st.checkbox(item)
