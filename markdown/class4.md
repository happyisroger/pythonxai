## 一、顯示圖片（st.image）🖼️

### 1️⃣ 顯示一張圖片

```python
st.image("image/apple.png", width=300, caption="蘋果")
```

📌 重點：

- `st.image`：在網頁上顯示圖片
- `width`：圖片寬度
- `caption`：圖片下面的說明文字

👉 就像在網頁上貼一張照片，並加一句說明。

---

### 2️⃣ 一次顯示資料夾裡的所有圖片

```python
image_files = os.listdir("image")
```

📌 重點：

- `os.listdir()`：把資料夾裡的檔案名字全部拿出來
- 用 `for` 迴圈，一張一張顯示圖片

👉 就像打開資料夾，把裡面的照片全部秀出來。

---

### 3️⃣ 自動符合畫面寬度

```python
st.image(image_path, use_container_width=True)
```

📌 重點：

- 圖片會自動變大或變小，剛好放進畫面

---

## 二、下拉選單（selectbox）⬇️

```python
selected_image = st.selectbox("請選擇圖片", image_files)
```

📌 重點：

- `selectbox`：讓使用者用「下拉選單」選東西
- 選到的東西會存進 `selected_image`

👉 就像點餐時選飲料口味。

---

## 三、網頁提示訊息（success / error）💬

### 四種常見訊息

- `st.success()`：成功 ✅
- `st.error()`：錯誤 ❌
- `st.warning()`：警告 ⚠️
- `st.info()`：資訊 ℹ️

📌 重點：

- 按下按鈕 → 顯示對應的訊息
- `st.rerun()`：重新整理網頁

---

## 四、購物平台（小型商店）🛒

### 1️⃣ 使用 session_state 記住資料

```python
ss = st.session_state
```

📌 重點：

- `session_state` 就像「網頁的記憶本」
- 關掉網頁前，資料不會不見

---

### 2️⃣ 商品資料

每個商品都有：

- 圖片
- 價格 💰
- 庫存 📦

```python
ss.products = {
    "apple": {"price":10, "stock":10}
}
```

---

### 3️⃣ 點「購買」會發生什麼？

- 庫存 > 0 → 買成功，庫存 -1
- 庫存 = 0 → 顯示「庫存不足」

👉 跟真的網路商店一樣！

---

### 4️⃣ 新增商品庫存

```python
ss.products[selected_product]["stock"] += add_stock
```

📌 重點：

- 可以幫商品「補貨」

---

## 五、函式（function）📦

### 1️⃣ 最簡單的函式

```python
def hello():
    print("hello")
```

📌 重點：

- 函式＝把事情包起來
- 需要時再叫它來做事

---

### 2️⃣ 有名字的函式

```python
def greet(name):
    print("Hello", name)
```

👉 傳名字進去，函式會說你好。

---

### 3️⃣ 函式回傳答案（return）

```python
def two_num_min(a, b):
    return a if a < b else b
```

📌 重點：

- `return`：把答案帶回來

---

## 六、預設值（有備用答案）🧮

```python
def calculate_circle_area(radius, pi=3.14):
```

📌 重點：

- 如果沒有給 `pi`，就用 3.14
- 有給就用新的

👉 就像有「預設設定」。

---

## 七、全域變數 & 區域變數 🌍📍

### 1️⃣ 全域變數（外面）

```python
length = 5
```

👉 全部的人都看得到

---

### 2️⃣ 區域變數（函式裡）

```python
def calculate():
    area = length * length
```

👉 只有函式裡面能用

---

### 3️⃣ global（不常用）

```python
global area
```

📌 重點：

- 可以讓函式改外面的變數
- **新手不建議常用**，容易搞混

---

## ⭐ 今日重點總整理

✔ 可以顯示圖片、做下拉選單
✔ 可以做簡單的購物網站
✔ 函式可以幫忙算事情
✔ `session_state` 可以記住資料
✔ 變數有「外面」和「裡面」的差別
