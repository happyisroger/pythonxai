import streamlit as st

st.title("排版練習")

co11, co12 = st.columns(2)
if co11.button("氣球按鈕"):
    co11.balloons()
if co12.button("雪花按鈕"):
    co12.snow()

co13, co14, co15 = st.columns([1, 2, 3])
with co13:
    st.write("這在 co13")
    st.button("按鈕3")
with co14:
    st.write("這在 co14")
    st.button("按鈕4")
with co15:
    st.write("這在 co15")
    st.button("按鈕5")

numCol = st.number_input("請輸入欄位數量", min_value=1, value=3, step=1)
numButton = st.number_input("請輸入按鈕數量", min_value=1, step=1)
cols = st.columns(numCol)
for i in range(numButton):
    cols[i % numCol].button(f"Button [{i + 1}]")

st.title("文字輸入元件")
text = st.text_input("")
st.write("你輸入的文字是: " + text)
