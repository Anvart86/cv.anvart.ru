# cv.anvart.ru — сайт-визитка

Онлайн-резюме с интерактивным просмотром BIM-модели прямо в браузере.
Живая версия: **[cv.anvart.ru](https://cv.anvart.ru)**

## Стек

- **Фронтенд:** vanilla HTML/CSS/JS, без фреймворков и сборки — один `index.html`
- **3D:** [Autodesk Platform Services Viewer](https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/overview/) v7 (стриминг модели из облака, ленивая загрузка по клику)
- **Инфраструктура:** Docker + nginx (`nginx:alpine`), HTTPS через Caddy
- **Тема:** светлая/тёмная, `prefers-color-scheme` + переключатель
- **SEO:** JSON-LD (`Person`), Open Graph, `sitemap.xml`, `robots.txt`

## Структура

```
index.html        — вся страница: разметка, стили, скрипты, вьювер
Dockerfile        — образ на базе nginx:alpine
nginx.conf        — конфиг веб-сервера
fonts/            — Inter (woff2, латиница + кириллица)
photo.*           — фото, og-image, favicon-набор
cv-tukhvatullin.pdf — резюме в PDF
```

## Авторизация вьювера

Вьювер получает токен Autodesk из `token.json`, который генерируется **на сервере** по расписанию
(cron, каждые 50 минут — TTL токена 60 минут) и в репозиторий не попадает.
Ключи приложения APS хранятся в `.env` на сервере; `.env`, `token.json` и скрипты обновления токена
исключены через `.gitignore`.

## Локальный запуск

```bash
docker build -t cv-site .
docker run --rm -p 8080:80 cv-site
# http://localhost:8080 — страница откроется, 3D потребует своего token.json
```

## Автор

**Анвар Тухватуллин** — BIM/ТИМ, цифровизация строительства.
[cv.anvart.ru](https://cv.anvart.ru)
