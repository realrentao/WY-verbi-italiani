import sys, json
from playwright.sync_api import sync_playwright

HTML = r"D:\workbuddy工作区\2026-09-07-14-57-58\verbo-italiano.html"
OUT = r"D:\workbuddy工作区\2026-09-07-14-57-58\_verify"

import os
os.makedirs(OUT, exist_ok=True)

errors = []
console_errs = []

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(channel="msedge", headless=True)
    except Exception as e:
        print("msedge channel failed, fallback to bundled chromium:", e)
        browser = p.chromium.launch(headless=True)

    page = browser.new_page(viewport={"width":1280,"height":800})
    page.on("console", lambda m: console_errs.append(m.text) if m.type=="error" else None)
    page.on("pageerror", lambda e: errors.append(str(e)))

    page.goto("file:///" + HTML.replace("\\","/"), wait_until="networkidle")
    page.wait_for_selector("#vcount", timeout=15000)
    page.wait_for_timeout(800)

    vcount = page.inner_text("#vcount").strip()
    vlist_count = page.eval_on_selector_all("#vlist .vitem", "els => els.length")
    idx_count = page.eval_on_selector_all("#idx .letter, #idx li, #idx a", "els => els.length")

    # abrir un verbo (es: "essere") clicando en la lista
    # buscar via search box
    page.fill("#search", "essere")
    page.wait_for_timeout(300)
    page.click("#vlist .vitem", timeout=8000)
    page.wait_for_timeout(500)
    title = page.inner_text("#vtitle").strip()
    tense_rows = page.eval_on_selector_all("#detail .tense, #detail .mood", "els => els.length")

    # logo
    logo_ok = page.eval_on_selector(".logo", "el => (el.tagName==='IMG' ? (el.naturalWidth>0) : (el.offsetWidth>0))") if page.query_selector(".logo") else False

    page.screenshot(path=OUT+"/desktop.png")

    # mobile
    m = browser.new_page(viewport={"width":390,"height":844})
    m.goto("file:///" + HTML.replace("\\","/"), wait_until="networkidle")
    m.wait_for_selector("#vcount", timeout=15000)
    m.wait_for_timeout(500)
    m.screenshot(path=OUT+"/mobile.png")

    browser.close()

print("vcount_text:", vcount)
print("vlist_rendered_items:", vlist_count)
print("idx_letters:", idx_count)
print("clicked_title:", title)
print("detail_tense_or_mood_blocks:", tense_rows)
print("logo_loaded:", logo_ok)
print("page_errors:", errors)
print("console_errors:", console_errs)
print("ACCEPTANCE:", "PASS" if (not errors and not console_errs and "664" in vcount and logo_ok) else "CHECK")
