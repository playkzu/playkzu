# 堡量建設 Flask 首頁

## 啟動

在此目錄開啟 PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

開啟 http://127.0.0.1:5000 。以 Ctrl+C 停止。

## 修改內容

- `app.py`：建案清單。
- `templates/index.html`：品牌文案、電話、地址、電子信箱。
- `static/css/style.css`：配色、桌機與手機版面。
- `static/images/architecture.svg`：原創建築示意圖，可替換為正式建案照片。
- `static/js/main.js`：手機選單、建案介紹彈窗。

目前品牌文案為提案，建案資料及狀態為示意待確認；沒有虛構公司年資、業績數字、電話或地址。聯絡區目前僅展示待補資訊，尚無送出表單、寄信或預約功能。

参考網站：https://www.jut.com.tw/ 、https://www.fu-yu.com/ 。僅參考導覽與內容架構，未複製其圖片、原始碼或文案。

本機使用 Flask 開發伺服器。正式上線前，應確認品牌與建案資料並使用正式 WSGI 服務部署。
