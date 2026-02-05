## 🖥️ 一、Streamlit 是什麼？

👉 Streamlit 可以把程式變成「**可以按、可以輸入的畫面**」，像小網站一樣。

```python
import streamlit as st
```

✔ 先請 Streamlit 來幫忙

---

## 🏷️ 二、標題與顯示文字

```python
st.title("標題文字")
st.write("要顯示的內容")
```

- `st.title`：顯示大標題
- `st.write`：顯示文字或數字

---

## 🔢 三、數字輸入框（number_input）

```python
number = st.number_input("請輸入一個數字",
                         min_value=0,
                         max_value=100,
                         value=50,
                         step=1)
```

✔ 可以設定

- 最小值
- 最大值
- 預設值
- 一次加多少

---

## 📝 四、成績等第判斷（if 判斷）

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"
```

👉 電腦會「照順序檢查」
👉 只會做**第一個符合的**

---

## 🎈 五、按鈕與特效

```python
if st.button("點我"):
    st.balloons()
```

- `st.button()`：做一個按鈕
- `st.balloons()`：放氣球
- `st.snow()`：下雪 ❄️

---

## 🔁 六、重複做事情（for 迴圈）

### 1️⃣ 重複 5 次

```python
for i in range(5):
    print("hello")
```

### 2️⃣ 從 2 到 5

```python
for i in range(2, 6):
    print(i)
```

### 3️⃣ 每次跳 2

```python
for i in range(2, 10, 2):
    print(i)
```

---

## 🔺 七、數字金字塔

```python
for i in range(1, height + 1):
    st.write(str(i) * i)
```

👉 `str(i) * i`

- 把數字變文字
- 重複顯示

---

## ⭐ 八、箭頭金字塔

- 用「空白 + 星星」排出形狀
- `\n` 表示換行

---

## 📦 九、清單（List）

### 不同種類的清單

```python
[1, 2, 3]
["apple", "banana"]
[1, "apple", True]
```

### 巢狀清單

```python
[1, 2, [3, 4]]
```

---

## 🔍 十、從清單拿東西

```python
L = [1, 2, [3, 4]]
L[0]      # 1
L[2][0]   # 3
```

👉 電腦是「從 0 開始算」

---

## ✂️ 十一、清單切片

```python
L[1:4]      # 從第 1 到第 3
L[::2]      # 每隔一個拿
```

---

## 📏 十二、清單長度

```python
len([1, 2, 3])  # 3
```

---

## 🔄 十三、走訪清單

### 方法 1

```python
for i in range(len(L)):
    print(L[i])
```

### 方法 2（比較簡單 👍）

```python
for item in L:
    print(item)
```

---

## ✏️ 十四、修改清單

```python
a[0] = 10
```

⚠️ 指向同一個清單時要小心：

```python
b = a
```

---

## ➕➖ 十五、清單常用功能

```python
append()   # 加東西
remove()   # 移除指定
pop()      # 移除最後或指定
sort()     # 排順序
```

---

## 📁 十六、讀取檔案

```python
with open("檔名", "r", encoding="utf-8") as f:
    content = f.read()
```

---

## 📂 十七、找資料夾裡的檔案

```python
os.listdir("資料夾")
```

✔ `endswith(".md")`
👉 檢查檔名是不是 `.md`

---

## 🧱 十八、畫面排版（columns）

```python
col1, col2 = st.columns(2)
```

👉 可以把畫面分成多欄

---

## 🔤 十九、文字輸入框

```python
text = st.text_input("")
```

---

## 🧠 二十、Session State（記住數字）

```python
st.session_state
```

✔ 可以讓數字「按了還記得」
✔ 不會每次歸零

---

## ⭐ 今天最重要的重點

- Streamlit 可以做互動畫面
- `if` 用來判斷
- `for` 用來重複
- `list` 是裝很多東西的盒子
- `session_state` 可以記住資料
