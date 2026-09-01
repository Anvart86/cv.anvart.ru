# Генератор cv-tukhvatullin.pdf из текстов index.html (зеркалить правки вручную).
# Запуск: python3 tools/gen_pdf.py   (нужен playwright + chromium)
import asyncio, base64, pathlib
from playwright.async_api import async_playwright

CV = pathlib.Path(__file__).resolve().parent.parent  # корень репозитория
def b64(p, mime): return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()
cyr = b64(CV/'fonts/inter-cyrillic.woff2','font/woff2')
lat = b64(CV/'fonts/inter-latin.woff2','font/woff2')
photo = b64(CV/'photo.png','image/png')

HTML = f"""<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><style>
@font-face{{font-family:'Inter';font-weight:400 800;font-display:block;src:url({cyr}) format('woff2');
  unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;}}
@font-face{{font-family:'Inter';font-weight:400 800;font-display:block;src:url({lat}) format('woff2');
  unicode-range:U+0000-00FF,U+2000-206F,U+20AC,U+2122,U+2212;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Inter',sans-serif;color:#1f2937;font-size:10.2pt;line-height:1.5;}}
.page{{padding:34px 44px;}}
header{{display:flex;gap:22px;align-items:center;border-bottom:2px solid #111827;padding-bottom:16px;margin-bottom:16px;}}
.photo{{width:96px;height:96px;border-radius:50%;object-fit:cover;flex:none;}}
h1{{font-size:23pt;font-weight:800;letter-spacing:-0.02em;color:#030712;}}
.role{{font-size:12pt;color:#374151;margin-top:2px;font-weight:600;}}
.contacts{{font-size:8.8pt;color:#4b5563;margin-top:8px;line-height:1.7;}}
.contacts a{{color:#4b5563;text-decoration:none;}}
.contacts span{{white-space:nowrap;}}
.sep{{color:#d1d5db;margin:0 7px;}}
.summary{{font-size:10.2pt;color:#374151;margin-bottom:16px;}}
h2{{font-size:10.5pt;font-weight:800;text-transform:uppercase;letter-spacing:0.06em;color:#111827;
  border-bottom:1px solid #e5e7eb;padding-bottom:4px;margin:14px 0 9px;}}
.item{{margin-bottom:11px;}}
.ihead{{display:flex;justify-content:space-between;align-items:baseline;gap:12px;}}
.co{{font-weight:700;color:#111827;font-size:10.6pt;}}
.per{{font-size:8.8pt;color:#6b7280;white-space:nowrap;flex:none;}}
.pos{{font-size:9.8pt;color:#374151;font-style:italic;margin:1px 0 3px;}}
.desc{{font-size:9.6pt;color:#374151;}}
.eff{{background:#fef3c7;padding:1px 6px;border-radius:4px;font-weight:600;color:#111827;white-space:nowrap;}}
.tags{{display:flex;flex-wrap:wrap;gap:5px;margin-top:7px;}}
.tag{{font-size:8.6pt;background:#f3f4f6;color:#374151;padding:2px 8px;border-radius:5px;}}
.two{{display:flex;gap:26px;}} .two>div{{flex:1;}}
.row{{display:flex;justify-content:space-between;font-size:9.6pt;padding:2px 0;}}
.muted{{color:#6b7280;}}
.pub{{font-size:9.4pt;color:#374151;margin:3px 0;}}
a{{color:#111827;}}
@page{{size:A4;margin:0;}}
</style></head><body><div class="page">

<header>
  <img class="photo" src="{photo}">
  <div>
    <h1>Анвар Тухватуллин</h1>
    <div class="role">Руководитель по цифровизации строительства</div>
    <div class="contacts">
      <span>📍 Челябинск, Россия · Готов к переезду</span><br>
      <span>📞 +7 919 345-32-94</span><span class="sep">·</span>
      <span>✉ tuhvatullin@mail.ru</span><span class="sep">·</span>
      <span>🌐 cv.anvart.ru</span><span class="sep">·</span>
      <span>in/anvar-tukhvatullin</span><span class="sep">·</span>
      <span>Telegram @Anvart86</span>
    </div>
  </div>
</header>

<div class="summary">16+ лет в строительстве — от прораба до руководителя цифровизации. Внедряю 5D BIM и AI-автоматизацию с измеримой отдачей: экономический эффект ~40 млн ₽ за последний год. Считаю стоимость на ранних этапах прямо из BIM-моделей, перевожу исполнительную документацию в цифру, снимаю рутину с команды с помощью AI-автоматизации.</div>

<h2>Опыт работы</h2>

<div class="item">
  <div class="ihead"><span class="co">Голос.Девелопмент — Руководитель отдела технологий информационного моделирования</span><span class="per">Сен 2024 — н.в.</span></div>
  <div class="desc">Возглавляю ТИМ-отдел заказчика — команда 3 человека: обучение, мотивация и развитие сотрудников. Запустил расчёт стоимости на ранних этапах прямо из BIM-моделей (5D QTO): ВОР собирается из модели, вручную остаётся только проверка. С 2-го полугодия 2024 себестоимость новых объектов считается из BIM-модели. Внедрил в компании EIR-требования заказчика для BIM-проектов и Среду Общих Данных (Signal Docs). Опыт сдачи цифровой исполнительной документации на 2 объектах. Оптимизирую технические решения на основе BIM-данных. По внутренним опросам около 80% инженеров и ИТР используют BIM-модели в работе. ГОЛОС — 6-е место в Индексе инновационности девелоперов 2026 (Сколково / ВЭБ.РФ). <span class="eff">Экономический эффект: ~40 млн ₽/год</span> (логистика, тендеры, снабжение, СОД, цифровая ИД). Автоматизирую рутинную работу с данными через AI-агентов и LLM; методом AI-assisted разработки собираю внутренние инструменты — от идеи до прод-деплоя.</div>
</div>

<div class="item">
  <div class="ihead"><span class="co">Голос.Девелопмент — BIM-менеджер</span><span class="per">Фев 2023 — Сен 2024</span></div>
  <div class="desc">Реанимировал и вывел в боевую эксплуатацию «Меркурий» — QTO-приложение, которое считает объёмы работ прямо из BIM-модели. Внедрил расчёт себестоимости на основных этапах проекта: второй год компания считает себестоимость по BIM. Разработал корпоративный классификатор строительных работ в 1С УСО — единый язык для сметы и ERP.</div>
</div>

<div class="item">
  <div class="ihead"><span class="co">Голос.Девелопмент — Инженер ПТО 1-й категории</span><span class="per">Янв 2016 — Фев 2023</span></div>
  <div class="desc">Составлял объектные калькуляции и заявки по чертежам, рассчитывал себестоимость строительства. Проверял закрытие объёмов и расценки работ (КС-2), формы М-29. Выдавал рабочую документацию и вёл её входной контроль, разрабатывал нормы расхода материалов. Участвовал во внедрении ERP и переводе документооборота в цифру.</div>
</div>

<div class="item">
  <div class="ihead"><span class="co">Доступное жильё — Начальник участка</span><span class="per">Июн 2013 — Янв 2016</span></div>
  <div class="desc">Руководил участком 12 000 м² жилья: 120 человек, 3 башенных крана. Освоил новую для Челябинска серию домов из сборно-монолитного каркаса.</div>
</div>

<div class="item">
  <div class="ihead"><span class="co">Атомстройкомплекс — Заместитель начальника ПТО</span><span class="per">Июл 2012 — Июн 2013</span></div>
  <div class="desc">Техническое сопровождение строительства, контроль себестоимости, технико-экономическое сравнение материалов. Внедрил механические муфты вместо ванной сварки — ускорил и удешевил соединение арматуры.</div>
</div>

<div class="item">
  <div class="ihead"><span class="co">Трест Строймонолит / БЕТОТЕК / Ферт — Инженер ПТО / Производитель работ</span><span class="per">2009 — 2012</span></div>
  <div class="desc">Строительство цементного завода и производство ЖБИ. Автоматизировал списание материалов (форма М-29) в 1С.</div>
</div>

<h2>Ключевые проекты</h2>
<div class="desc">
  <b>Меркурий</b> (mercurius.golos.click) — 5D-расчёт объёмов и себестоимости из BIM: 13 проектов / 464 966 м², точность к факту в пределах 5%, ВОР за неделю вместо месяца, −8 259 чел-ч; тендеры по моделям на объём свыше 1 млрд ₽. &nbsp;•&nbsp;
  <b>Revit-ферма (AI-агенты)</b> — автономные агенты на Revit: подготовка строительной модели, проверка рабочей и сметной документации, ежесуточные сводки по проекту; ночная ферма на нескольких версиях Revit с автоматической самопроверкой объёмов (опытное тестирование). &nbsp;•&nbsp;
  <b>Цифровая исполнительная документация</b> — перевод ИД в цифру через СОД (Signal Docs / EXON) на 2 объектах: 204 участника, РД за 1 минуту вместо 15 дней, эффект ~10 млн ₽/год. &nbsp;•&nbsp;
  <b>AI-автоматизация</b> — AI-агенты, LLM и n8n-сценарии: аудит ведомостей объёмов и калькуляций перед выгрузкой в 1С (задвоения, количества, цены против рынка), проверка дублей документации в СОД с отчётом в Telegram и на почту, ежесуточные сводки Revit-фермы. &nbsp;•&nbsp;
  <b>AI-assisted разработка</b> — в связке с ИИ собрал плагин AgentTIM для Revit (C#, 2020–2027) и ферму на нём, сервис аудита смет (Python/FastAPI) со встройкой в Меркурий, инфобот по объёмам объектов, модули Меркурия (React/.NET); полный цикл от идеи до деплоя.
</div>

<h2>Преподавание</h2>
<div class="item">
  <div class="ihead"><span class="co">ЮУрГУ — Цифровая кафедра · Приглашённый преподаватель</span><span class="per">2025 / 2026</span></div>
  <div class="desc">Веду модуль «Количественный анализ BIM-моделей» в программе допквалификации «Цифровое информационное моделирование в промышленном и гражданском строительстве»: извлечение объёмов работ из BIM-моделей, привязка элементов к расценкам, 5D BIM / QTO на реальных кейсах.</div>
</div>

<h2>Публикации и медиа</h2>
<div class="pub">📄 Кейс «BIM на стройке: про выгоду, а не моду. Опыт Голос.Девелопмент» — cifrastroy.ru</div>
<div class="pub">📰 Публикация в медиа «Цифровая трансформация Челябинска»</div>

<h2>Навыки</h2>
<div class="tags">
  <span class="tag">BIM / ТИМ</span><span class="tag">Autodesk Revit</span><span class="tag">5D BIM / QTO</span>
  <span class="tag">EXON</span><span class="tag">ЦУС</span><span class="tag">Signal Docs</span><span class="tag">Autodesk CC</span>
  <span class="tag">1С УСО / ERP</span><span class="tag">MS Excel</span><span class="tag">LLM / AI-агенты</span>
  <span class="tag">AI-assisted разработка</span><span class="tag">N8N</span><span class="tag">EIR разработка</span>
  <span class="tag">Управление командой</span><span class="tag">Сметное дело</span>
</div>

<div class="two" style="margin-top:14px;">
  <div>
    <h2 style="margin-top:0;">Образование</h2>
    <div class="row"><span>Южно-Уральский гос. университет<br><span class="muted">Архитектурно-строительный, ПГС — Специалист</span></span><span class="per">2009</span></div>
    <h2>Языки</h2>
    <div class="row"><span>Русский</span><span class="muted">Родной</span></div>
    <div class="row"><span>Английский</span><span class="muted">B1 — Средний</span></div>
  </div>
  <div>
    <h2 style="margin-top:0;">Сертификаты</h2>
    <div class="row"><span><a href="https://pssbim.ru/pbs-bim-manager-certificate/">BIM Manager «Design» — ПБС/PBC, Международная система сертификации BIM-менеджеров (ООО «ПСС»), сертификат PBC.BM.24.12</a> <span class="muted">· проверка: pssbim.ru</span></span><span class="per">2024</span></div>
    <div class="row"><span>Курс «BIM-менеджер» — ПСС, одобрен Университетом Минстроя России: Revit, Navisworks, BIM 360, Solibri, Vitro-CAD, NanoCAD, Renga</span><span class="per">2024</span></div>
    <div class="row"><span>Эффективный руководитель — Н.В. Гаврилова</span><span class="per">2023</span></div>
    <div class="row"><span>English Intermediate — The English Club</span><span class="per">2022</span></div>
  </div>
</div>

<h2>Личное</h2>
<div class="desc">🏃 Август 2026 — пробежал первый марафон (42.2 км) за 3:57, выбежал из целевых 4 часов. AI-тренер собственной разработки: автоматический сбор метрик (пульс, темп, объём), ИИ-анализ и корректировка тренировочной программы под целевые показатели — тот же контур «данные → аналитика → решение», что и в девелопменте.</div>

</div></body></html>"""

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.set_content(HTML, wait_until='networkidle')
        await pg.wait_for_timeout(400)
        await pg.pdf(path=str(CV/'cv-tukhvatullin.pdf'), format='A4', print_background=True,
                     margin={'top':'0','bottom':'0','left':'0','right':'0'})
        await b.close()
        print('cv-tukhvatullin.pdf сгенерирован')

asyncio.run(main())
