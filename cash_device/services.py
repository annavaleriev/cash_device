import io
from collections import Counter
from datetime import datetime

import pdfkit
import qrcode
from django.conf import settings
from django.core.files.base import ContentFile
from django.template.loader import render_to_string

from cash_device.models import Item, Receipt


class PDFReceiptGenerator:
    """Генератор PDF-чека, который принимает список товаров и генерирует чек в формате PDF."""

    def __init__(self, items: list[Item]):
        items_counter = Counter(items)  # Счётчик товаров, чтобы избежать дублирования
        self.__items = []
        for item, count in items_counter.items():
            self.__items.append(
                {
                    "title": item.title,  # Название товара
                    "price": item.price,  # Цена товара
                    "count": count,  # Количество товара в чеке
                    "total_price": item.price
                    * count,  # Общая цена для данного товара (цена * количество)
                }
            )

        # self.__items = items  # Список товаров, которые будут в чеке
        # self.__total_sum = sum([item.price for item in items]) # Сумма всех товаров в чеке
        self.__total_sum = sum(item["total_price"] for item in self.__items)
        self.__day_time_now = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S.%f"
        )  # Текущая дата и время в формате "ГГГГ-ММ-ДД ЧЧ:ММ:СС.микросекунды"
        self.__file_name = f"receipt_{self.__day_time_now}_{self.__total_sum}.pdf"  # Имя файла чека, которое будет использоваться при сохранении в базу данных

    def __generate_html(self):
        """Генерирует HTML-чек из шаблона receipt_template.html, подставляя туда товары, сумму и дату."""
        return render_to_string(
            "receipt_template.html",
            {
                "items": self.__items,
                "total_price": self.__total_sum,
                "day_time_now": self.__day_time_now,
                "company_name": settings.COMPANY_NAME,
                "kkm": settings.KKM,
                "inn": settings.INN,
            },
        )

    def generate(self):
        """Генерирует PDF-файл чека из HTML-шаблона и сохраняет его в базу данных."""
        html_information = self.__generate_html()
        pdf = pdfkit.from_string(html_information)
        file = ContentFile(pdf, name=self.__file_name)
        return Receipt.objects.create(file=file)


class QRCodeGenerator:
    """Генератор QR-кода, который принимает строку и возвращает QR-код в виде байтового потока."""

    def __init__(self, str_to_qr_code: str):
        self.__str_to_qr_code = str_to_qr_code

    def generate(self):
        # Создаём QR-код как изображение (PIL Image)
        qr_img = qrcode.make(self.__str_to_qr_code)

        # Буфер в памяти, имитирует файл
        buffer = io.BytesIO()

        # Сохраняем картинку в PNG-формате в буфер
        qr_img.save(buffer, format="PNG")

        # Возвращаемся к началу буфера
        buffer.seek(0)

        # Возвращаем байтовый поток PNG
        return buffer
