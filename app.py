"""堡量建設形象網站。"""
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

PROJECTS = [
    {"name": "新溝段新案", "category": "規劃中", "description": "從土地出發，描繪下一段生活風景。", "detail": "此區塊為展示示意，正式案名、基地位置與規劃內容待確認後更新。", "style": "one"},
    {"name": "梧鳳段建案", "category": "建案展示", "description": "讓家的尺度，回應日常的每一份期待。", "detail": "此區塊為展示示意，銷售狀態、建築規格與完工時間待確認後更新。", "style": "two"},
    {"name": "歷年建築作品", "category": "作品實績", "description": "一磚一瓦，累積值得託付的建築風景。", "detail": "歷年作品照片、名稱與完工資訊待補，畫面使用原創建築示意圖。", "style": "three"},
]

@app.get("/")
def index():
    return render_template("index.html", projects=PROJECTS, year=datetime.now().year)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
