import io
from datetime import datetime

import pdfkit
import qrcode
from django.conf import settings
from django.core.files.base import ContentFile
from django.db.models import QuerySet
from django.template.loader import render_to_string

from cash_device.models import Item, Receipt


class PDFReceiptGenerator:
    def __init__(self, items: list[Item]):
        self.__items = items
        self.__total_sum = sum([item.price for item in items])
        self.__day_time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.__file_name = f"receipt_{self.__day_time_now}_{self.__total_sum}.pdf"

    def __generate_html(self):
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
        html_information = self.__generate_html()
        pdf = pdfkit.from_string(html_information)
        file = ContentFile(pdf, name=self.__file_name)
        return Receipt.objects.create(file=file)


class QRCodeGenerator:
    def __init__(self, str_to_qr_code: str):
        self.__str_to_qr_code = str_to_qr_code

    def generate(self):
        qr = qrcode.QRCode()
        qr.add_data(self.__str_to_qr_code)
        f = io.StringIO()
        return qr.print_ascii(out=f)
        # return qrcode.make(self.__str_to_qr_code)


class CashMachineService:
    def __init__(self, items: QuerySet[Item]):
        self.__items = items


    def get_qr_receipt(self) -> ...:
        ...


