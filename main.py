import streamlit as st

question_1 = "Comparing the two full faces (Left and Right), which one looks more realistic?"
options_1 = ["The Left one looks more realistic", "The Right one looks more realistic"]
question_2 = "Comparing the lips of two faces, which one is more in sync with audio?"
options_2 = ["The Left one is more in sync with audio", "The Right one is more in sync with audio"]

# 显示问题并获取用户的答案
answer_1 = st.radio(label=question_1, options=options_1, key=fr"button1")
answer_2 = st.radio(label=question_2, options=options_2, key=fr"button2")
