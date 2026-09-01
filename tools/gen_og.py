# Генератор og-image (1200×630, рендер scale 2) для превью в Telegram/соцсетях.
# Запуск: python3 tools/gen_og.py   (нужен playwright + chromium)
import asyncio, base64, pathlib
from playwright.async_api import async_playwright

CV = pathlib.Path(__file__).resolve().parent.parent  # корень репозитория
def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()

cyr  = b64(CV/'fonts/inter-cyrillic.woff2', 'font/woff2')
lat  = b64(CV/'fonts/inter-latin.woff2', 'font/woff2')
photo= b64(CV/'photo.png', 'image/png')

HTML = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Inter';font-style:normal;font-weight:400 800;font-display:block;
  src:url({cyr}) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;}}
@font-face{{font-family:'Inter';font-style:normal;font-weight:400 800;font-display:block;
  src:url({lat}) format('woff2');unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2122,U+2212;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:1200px;height:630px;}}
body{{font-family:'Inter',sans-serif;background:#ffffff;color:#030712;position:relative;overflow:hidden;}}
.topbar{{position:absolute;top:0;left:0;right:0;height:14px;background:#111827;}}
.wrap{{display:flex;align-items:center;height:100%;padding:0 90px;gap:56px;}}
.photo{{width:196px;height:196px;border-radius:50%;object-fit:cover;flex:none;
  box-shadow:0 0 0 6px #f3f4f6;}}
.col{{flex:1;}}
.name{{font-size:60px;font-weight:800;letter-spacing:-0.03em;line-height:1.02;}}
.subtitle{{font-size:29px;font-weight:500;color:#374151;margin-top:12px;letter-spacing:-0.01em;}}
.rule{{height:1px;background:#e5e7eb;margin:26px 0 22px;}}
.line{{font-size:26px;color:#111827;margin-bottom:12px;}}
.tags{{font-size:26px;color:#111827;margin-bottom:16px;}}
.tags b{{font-weight:600;}}
.eff{{display:inline-block;font-size:26px;font-weight:600;color:#111827;
  background:#fef3c7;padding:6px 14px;border-radius:8px;}}
.foot{{font-size:22px;color:#6b7280;margin-top:24px;}}
.foot b{{color:#374151;font-weight:600;}}
</style></head><body>
<div class="topbar"></div>
<div class="wrap">
  <img class="photo" src="{photo}">
  <div class="col">
    <div class="name">Анвар Тухватуллин</div>
    <div class="subtitle">Руководитель по цифровизации строительства</div>
    <div class="rule"></div>
    <div class="line">16+ лет в строительной отрасли</div>
    <div class="tags">BIM / ТИМ &nbsp;•&nbsp; 5D QTO &nbsp;•&nbsp; AI-автоматизация</div>
    <div class="eff">Экономический эффект: ~40 млн ₽/год</div>
    <div class="foot">Челябинск, Россия &nbsp;•&nbsp; Готов к переезду &nbsp;•&nbsp; <b>cv.anvart.ru</b></div>
  </div>
</div>
</body></html>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1200,'height':630}, device_scale_factor=2)
        await pg.set_content(HTML, wait_until='networkidle')
        await pg.wait_for_timeout(400)
        await pg.screenshot(path=str(CV/'og-image-v3.png'), clip={'x':0,'y':0,'width':1200,'height':630})
        await b.close()
        print('og-image-v3.png сгенерирован')

asyncio.run(main())
