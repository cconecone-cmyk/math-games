#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import socket
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

def get_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

def run_server(port, folder):
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=folder, **kwargs)
        def log_message(self, format, *args):
            pass # suppress logging
    httpd = HTTPServer(('127.0.0.1', port), Handler)
    httpd.serve_forever()

def main():
    math_games_dir = r"c:\Users\User\Documents\Antigravity\math-games"
    out_dir = r"C:\Users\User\.gemini\antigravity\brain\5865bb9f-3467-450c-91c7-1d211ecc2e90"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "math_games_tabs_verify.png")

    port = get_free_port()
    t = threading.Thread(target=run_server, args=(port, math_games_dir), daemon=True)
    t.start()
    time.sleep(0.5)

    tabs = [
        ("games", "【分頁 1】數學對戰遊戲 (3D/2D FPS・質數海戰・卡牌對決)", "games.html"),
        ("lab", "【分頁 2】動態解題教室 (短除法v2.7・倍數判別・跑道速率・繩子連比・平行四邊形相似)", "lab.html"),
        ("theater", "【分頁 3】觀念動畫影廳 (劇院級 Cinema 放映・國三圓幾何・國一因倍數)", "theater.html"),
        ("tools", "【分頁 4】教師備課百寶箱 (MathGeoCraft幾何・EduPDF工具箱・字帖・表單復刻)", "tools.html")
    ]

    temp_images = []

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 920}, device_scale_factor=1)
        page = context.new_page()

        for tab_id, label, url_file in tabs:
            url = f"http://127.0.0.1:{port}/{url_file}"
            print(f"Navigating to {url}...")
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(800)

            shot_path = os.path.join(math_games_dir, f"temp_{tab_id}.png")
            page.screenshot(path=shot_path, full_page=False)
            img = Image.open(shot_path)
            temp_images.append((tab_id, label, img))
            print(f"Captured {tab_id} screenshot: {img.size}")

        browser.close()

    # Stitch into 2x2 grid
    # Each cell: 1440 x 920, plus top header 80px and cell title banner 40px
    cell_w, cell_h = 1440, 920
    banner_h = 44
    header_h = 90
    margin = 16

    grid_w = margin * 3 + cell_w * 2
    grid_h = header_h + margin * 3 + (cell_h + banner_h) * 2

    canvas = Image.new("RGB", (grid_w, grid_h), color=(11, 17, 32))
    draw = ImageDraw.Draw(canvas)

    # Load system font
    font_large = None
    font_cell = None
    try:
        # Windows font
        font_large = ImageFont.truetype("msjhbd.ttc", 36)
        font_cell = ImageFont.truetype("msjhbd.ttc", 22)
    except Exception:
        try:
            font_large = ImageFont.truetype("arialbd.ttf", 36)
            font_cell = ImageFont.truetype("arialbd.ttf", 22)
        except Exception:
            font_large = ImageFont.load_default()
            font_cell = ImageFont.load_default()

    # Draw main header
    header_title = "國中數學互動大廳 ｜ 四大獨立分頁架構視覺驗收總覽"
    header_sub = "徹底解決單一長頁混疊問題 ｜ 頂部導覽即時切換 ｜ 獨立網址分頁 ｜ 劇院放映影廳 ｜ 開源備課神器"
    draw.text((margin + 10, 16), header_title, fill=(56, 189, 248), font=font_large)
    draw.text((margin + 12, 58), header_sub, fill=(148, 163, 184), font=font_cell)

    positions = [
        (margin, header_h + margin),                               # Top Left (games)
        (margin * 2 + cell_w, header_h + margin),                  # Top Right (lab)
        (margin, header_h + margin * 2 + cell_h + banner_h),       # Bottom Left (theater)
        (margin * 2 + cell_w, header_h + margin * 2 + cell_h + banner_h) # Bottom Right (tools)
    ]

    for i, (tab_id, label, img) in enumerate(temp_images):
        x, y = positions[i]

        # Draw cell header pill
        draw.rectangle([x, y, x + cell_w, y + banner_h], fill=(30, 41, 59))
        draw.rectangle([x, y, x + cell_w, y + banner_h], outline=(56, 189, 248), width=1)
        draw.text((x + 16, y + 10), label, fill=(241, 245, 249), font=font_cell)

        # Paste screenshot
        canvas.paste(img, (x, y + banner_h))
        draw.rectangle([x, y + banner_h, x + cell_w, y + banner_h + cell_h], outline=(255, 255, 255, 40), width=1)

    canvas.save(out_path, format="PNG", optimize=True)
    print(f"Stitched verify sheet saved to: {out_path}")

    # Clean up temp shots
    for tab_id, _, _ in temp_images:
        p = os.path.join(math_games_dir, f"temp_{tab_id}.png")
        if os.path.exists(p):
            os.remove(p)

if __name__ == "__main__":
    main()
