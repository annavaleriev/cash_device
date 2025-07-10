# 💰 Cash Device

**Cash Device** — это Django-приложение, моделирующее работу кассового аппарата с возможностью создания чеков, генерации PDF-документов, и обработки товаров. Поддерживает управление через Django admin и REST API.

## 🚀 Возможности

- Управление товарами (название, цена).
- Создание кассовых чеков с несколькими товарами.
- Генерация PDF-файла чека с помощью `pdfkit` и `wkhtmltopdf`.
- Генерация QR-кода для каждого чека.
- Хранение PDF в базе данных через `ContentFile`.
- API с сериализацией данных и валидацией.
- Логика создания PDF-отчётов с рендерингом HTML-шаблонов.

## 🧱 Стек технологий

- Python 3.11+
- Django 4+
- Django REST Framework
- PostgreSQL / SQLite
- pdfkit + wkhtmltopdf
- qrcode
- Docker (опционально)
- pytest / unittest (опционально)

## 📁 Структура проекта

```
cash_register/
├── cash_device/             # Приложение кассового аппарата: логика чеков и товаров
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── services/            # Генерация PDF и QR-кодов
│       
├── config/                  # Конфигурация Django-проекта (settings, urls и пр.)
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/               # HTML-шаблоны для рендеринга чеков
├── media/                   # Хранение PDF-файлов и QR-кодов
├── Dockerfile               # Инструкция для сборки Docker-контейнера
├── docker-compose.yaml      # Конфигурация сервисов Docker Compose
├── .env_example             # Пример файла переменных окружения
├── manage.py                # Точка входа для Django
├── pyproject.toml           # Конфигурация Poetry и зависимостей
├── poetry.lock              # Зафиксированные зависимости
└── README.md                # Документация проекта

```

## ⚙️ Установка и запуск

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/annavaleriev/cash_device.git
   cd dds-cash

2. Создайте файл .env на основе .env_example и заполните его.

3. Запустите Docker-контейнеры:
   ```bash
   docker-compose up -d
   ```
4. Выполните миграции и создайте суперпользователя:
   ```bash
   docker-compose exec app python manage.py migrate
   docker-compose exec app python manage.py createsuperuser
   ```


## 📎 Полезные ссылки

- [wkhtmltopdf — официальный сайт](https://wkhtmltopdf.org/)
- [pdfkit документация](https://pypi.org/project/pdfkit/)
- [Django Docs](https://docs.djangoproject.com/)
- [DRF Docs](https://www.django-rest-framework.org/)

