# 國中數學互動大廳 ⚡ Math Games, Visual Lab & Video

專為國中數學打造的沉浸式互動遊戲、動態幾何解題實驗室、觀念動畫影廳與教師開源備課百寶箱！  
100% 純前端技術、免安裝、零後端依賴，支援電腦與平板即開即用。

🔗 **線上即用入口 (GitHub Pages)**：[https://cconecone-cmyk.github.io/math-games/](https://cconecone-cmyk.github.io/math-games/)

---

## 🌟 雙軌分頁與獨立頁面架構 (Multi-Tab & Standalone Architecture)

本網站徹底摒棄傳統單頁長卷式混雜堆疊，全面採用**頂部即時切換分頁列（Navbar Tabs）與獨立網址分頁（Standalone HTML）**雙軌架構。使用者可一鍵切換視圖、藉由網址 Hash (`#games`, `#lab`, `#theater`, `#tools`) 導航，或在新分頁直接開啟獨立單元：

| 分頁單元 | 獨立網址 / Hash | 核心內容與收錄項目 |
| :--- | :--- | :--- |
| **🎮 數學對戰遊戲** | [`games.html`](https://cconecone-cmyk.github.io/math-games/games.html) / `#games` | 3D 幾何射擊 FPS、心算射擊 MATH FPS、幾何勇者傳說 RPG、質數海戰棋、因倍數之戰卡牌對決 |
| **📐 動態解題教室** | [`lab.html`](https://cconecone-cmyk.github.io/math-games/lab.html) / `#lab` | 《短除法動態教室 v2.7》、`《倍數判別法動態教室》`、操場跑道速率、斷開繩子連比、平行四邊形相似推導 |
| **🎬 觀念動畫影廳** | [`theater.html`](https://cconecone-cmyk.github.io/math-games/theater.html) / `#theater` | 劇院級 Cinema 放映舞台：國三圓的幾何會考秒殺特輯（5 部）＋ 國一數與式因倍數幾何概念（3 部） |
| **🛠️ 教師備課百寶箱** | [`tools.html`](https://cconecone-cmyk.github.io/math-games/tools.html) / `#tools` | 開源備課神器：MathGeoCraft 幾何復刻、EduPDF 本地工具箱、灰底字描寫本生成器、Form Replicator 表單復刻 |

---

## 🕹️ 分頁 1：數學對戰遊戲 (Math Games)

1. **🔫 幾何小夥伴 3D 闖關 (Geometry FPS 3D)**
   - 檔案：[`geometry-fps-3d.html`](https://cconecone-cmyk.github.io/math-games/geometry-fps-3d.html)
   - 技術架構：Three.js 3D 渲染、PointerLockControls 視角鎖定、Raycaster 射擊判定。
   - 核心玩法：經典 CS 玩法的 3D 第一人稱射擊！支援鍵盤 WASD 走位、滑鼠鎖定視角瞄準、槍枝後座力動畫與即時射線判定，穿梭 3D 幾何戰場！
2. **🎯 數學射擊對戰 MATH FPS (2D 雙軌版)**
   - 檔案：[`math-fps.html`](https://cconecone-cmyk.github.io/math-games/math-fps.html)
   - 核心玩法：瞄準題目靶心，以最快速度扣下運算扳機！將心算融合為快節奏射擊對決，考驗極限運算手速。
3. **🔷 幾何勇者傳說冒險 (Geometry Quest 5.0)**
   - 檔案：[`geometry-quest.html`](https://cconecone-cmyk.github.io/math-games/geometry-quest.html)
   - 核心玩法：完整收錄國中課程！探索幾何地圖、解答章節任務、擊敗 BOSS 並解鎖成就系統。
4. **🚢 質數海戰 (Prime Battle)**
   - 檔案：[`prime-sea-battle.html`](https://cconecone-cmyk.github.io/math-games/prime-sea-battle.html)
   - 核心玩法：將質數判別與質因數分解化為海戰拆彈防禦戰！鎖定目標艦隊與炸彈密碼，精準辨識質數弱點一擊必殺！
5. **⚔️ 因倍數之戰 卡牌對決 (Factor & Multiple Battle)**
   - 教材手冊：[`docs/國中數學-因倍數之戰主題包-書冊.pdf`](https://cconecone-cmyk.github.io/math-games/docs/國中數學-因倍數之戰主題包-書冊.pdf)
   - 核心特色：融合最大公因數、最小公倍數與質因數分解的卡牌桌遊大作，附完整課堂活動主題包與學習單手冊。

---

## 📐 分頁 2：動態解題教室 (Dynamic Solving Lab)

1. **➗《短除法動態教室 v2.7》**（最新旗艦教具）
   - 線上教具：[https://cconecone-cmyk.github.io/short-division/](https://cconecone-cmyk.github.io/short-division/)
   - 核心特色：支援整數與標準分解式短除法運算、動態方格面積拼圖重組、長度倍數延伸與左右兩法對照，深刻理解公因數與公倍數幾何本質。
2. **🔍《倍數判別法動態教室》**（最新旗艦教具）
   - 線上教具：[https://cconecone-cmyk.github.io/divisibility-rules/](https://cconecone-cmyk.github.io/divisibility-rules/)
   - 核心特色：包含 2、4、8、3、9、11 及 7（三位分節法）的直觀幾何原理、位值切分與生動動畫演示，告別死記硬背。
3. **🏃 速率：同向與逆向跑操場動態解析**
   - 檔案：[`running-track-speed.html`](https://cconecone-cmyk.github.io/math-games/running-track-speed.html)
   - 核心特色：動態演示環形跑道上兩人「同向追趕（相距一圈）」與「逆向相遇（合走一圈）」的即時軌跡，滑桿自由調整速度與圈長。
4. **🪢 連比：斷開繩子動態解析**
   - 檔案：[`rope-ratio-split.html`](https://cconecone-cmyk.github.io/math-games/rope-ratio-split.html)
   - 核心特色：段考常考魔王題！將長度比例切割、重新綁定與分段以動態視覺化拖曳圖表呈現，一眼看穿比與實際長度的換算邏輯。
5. **📐 平行四邊形經典相似推導**
   - 檔案：[`parallelogram-similarity.html`](https://cconecone-cmyk.github.io/math-games/parallelogram-similarity.html)
   - 核心特色：平行四邊形內部截線形成的相似三角形群！即時動態著色標記對應邊與對應角，步驟式推導邊長幾何比例關係。

---

## 🎬 分頁 3：觀念動畫影廳 (Cinema Theater)

採用劇院級 Cinema 巨幕放映架構，配合下方影音清單隨點即播，零干擾、無廣告：

- **🏆 國三九上・圓的幾何大魔王系列**：
  1. 【EP01】點與圓的位置 ＆ 最值送分題 (26s)
  2. 【EP02】直線與圓 3 種關係 ＆ 坐標交點秒殺 (25s)
  3. 【EP03】弦心距垂徑定理 ＆ 必考水管水深題 (23s)
  4. 【EP04】雙切線鳶形 ＆ 會考壓軸三連擊 (25s)
  5. 【特別篇】圓的幾何大魔王破關總整理 (45s)
- **🌲 國一七上・數與式 ＆ 因倍數幾何概念系列**：
  6. 【七上】質數與合數直觀幾何概念 (28s)
  7. 【七上】埃拉托斯特尼 1~100 質數篩法 (33s)
  8. 【七上】標準分解式 ＆ 標準直式短除法 (32s)

---

## 🛠️ 分頁 4：教師備課百寶箱 (Teacher Toolbox)

1. **📐 MathGeoCraft 幾何圖秒級復刻**：[https://cconecone-cmyk.github.io/MathGeoCraft/](https://cconecone-cmyk.github.io/MathGeoCraft/)  
   貼上截圖當底圖，秒級復刻課本習作高解析圖檔 (PNG) 與 Word 試卷檔 (.docx)。
2. **📑 EduPDF Tools 教師備課 PDF 工具箱**：[https://cconecone-cmyk.github.io/edupdf-tools/](https://cconecone-cmyk.github.io/edupdf-tools/)  
   純前端本地運算無伺服器、智慧壓縮、單元拆分、合訂講義，快速處理考卷與教學文件。
3. **✍️ 線上灰底字描寫本生成器**：[https://cconecone-cmyk.github.io/copybook-generator/](https://cconecone-cmyk.github.io/copybook-generator/)  
   支援 A4 滿版硬筆字帖生成與列印，自訂教學文字、格線樣式與灰度，練字與班級輔導利器。
4. **📋 Form Replicator 表單 1:1 復刻神器**：[https://cconecone-cmyk.github.io/form-replicator/](https://cconecone-cmyk.github.io/form-replicator/)  
   智慧去手寫與印章、A4 雙面排版、Word 與向量 PDF 一鍵匯出，紙本表格數位化利器。
