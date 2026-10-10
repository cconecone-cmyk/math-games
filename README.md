# 國中數學互動遊戲大廳 (Math Games Hub)

🎮 收錄精選國中數學線上闖關、幾何探險與心算射擊對戰遊戲。免安裝、無後端依賴，支援電腦與平板即開即玩！

---

## 🕹️ 收錄遊戲清單

1. **🎯 數學射擊對戰 MATH FPS (v0.2.3)**
   - 檔案：`math-fps.html`
   - 特色：結合第一人稱射擊對戰與即時心算反應，瞄準題目靶心極速解題。
   - 適合年級：國中全階段心算與代數訓練。

2. **🔷 幾何小夥伴 Geometry Quest (v5.0)**
   - 檔案：`geometry-quest.html`
   - 特色：翰林版七上、七下、八上完整冒險地圖！結合幾何概念、題庫關卡與成就系統。
   - 適合年級：七年級至八年級幾何與代數單元。

---

## 🚀 如何發布到 GitHub 線上玩 (GitHub Pages)

本專案為 **100% 純前端靜態網頁架構**，無須任何伺服器即可直接透過 GitHub Pages 免費上線：

1. **建立 GitHub 儲存庫 (Repository)**：
   - 到 [GitHub.com](https://github.com) 點擊 **New repository**。
   - 命名為例如 `math-games`（設為 **Public** 公開）。
2. **上傳本資料夾的所有檔案**：
   - 包含：`index.html`、`math-fps.html`、`geometry-quest.html`、`README.md`。
   - 可直接使用網頁的「Upload files」按鈕拖曳上傳，或透過 Git 指令推送：
     ```bash
     git init
     git add .
     git commit -m "feat: initial math games hub release"
     git branch -M main
     git remote add origin https://github.com/<你的使用者名稱>/math-games.git
     git push -u origin main
     ```
3. **開啟 GitHub Pages 網站**：
   - 進入儲存庫的 **Settings** ➔ 側邊欄點擊 **Pages**。
   - 在 **Build and deployment** 下方的 **Branch** 選擇 `main` 分支、資料夾選 `/ (root)`，點擊 **Save**。
   - 等待約 1~2 分鐘，上方就會出現綠色的專屬線上網址：
     ```
     https://<你的使用者名稱>.github.io/math-games/
     ```
   - 點開即可線上遊玩！分享該網址給學生或家長，手機、平板、電腦皆可免安裝秒開！
