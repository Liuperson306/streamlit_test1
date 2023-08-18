import streamlit as st

def QA(data_face, data_lip, num):
    # 定义问题和选项
    question_1 = "Comparing the two full faces (Left and Right), which one looks more realistic?"
    options_1 = ["The Left one looks more realistic", "The Right one looks more realistic"]
    question_2 = "Comparing the lips of two faces, which one is more in sync with audio?"
    options_2 = ["The Left one is more in sync with audio", "The Right one is more in sync with audio"]

    # 显示问题并获取用户的答案
    answer_1 = st.radio(label=question_1, options=options_1, key=fr"button{num}.1")
    answer_2 = st.radio(label=question_2, options=options_2, key=fr"button{num}.2")

    # 以1/0数据保存
    ans1 = get_ans(answer_1)
    ans2 = get_ans(answer_2)

    # 保存结果到列表
    data_face[num-1] = ans1
    data_lip[num-1] = ans2

# 将用户的答案转化为1/0
def get_ans(answer_str):
    if "Left" in answer_str:
        return "1"
    elif "Right" in answer_str:
        return "0"

if "data_face" and "data_lip" not in st.session_state:
    # 初始化data变量
        data_face = [1 for x in range(0, 12)]
        data_lip = [1 for x in range(0, 12)]
    else:
        # 恢复data变量的状态
        data_face = st.session_state["data_face"]
        data_lip = st.session_state["data_lip"]

for num in range(12):
  QA(data_face, data_lip, num+1)
  st.write(data_face,data_lip)
