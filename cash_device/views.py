import os
from datetime import datetime

import pdfkit
import qrcode
from django.template.loader import render_to_string
from rest_framework.views import APIView, Response

from config import settings
from .models import Item
from .serializers import CashMachineSerializer
from rest_framework import status

'''

    Вход
    {
        'items': [1,2]
    }

    id name price
    1  тов1 333
    2  тов2 444
    33 + 444 =

    генерация чека и qrcode
    '''


class CashMachineView(APIView):
    def post(self, request):
        serializer = CashMachineSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        items_id = serializer.validated_data["items"]
        items = Item.objects.filter(id__in=items_id)

        total_price = sum(item.price for item in items)
        day_time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # html_information = render_to_string(
        #     "cash_device/receipt_template.html",
        #     {
        #         "items": items,
        #         "total_price": total_price,
        #         "day_time_now": day_time_now,
        #     },
        # )
        html_information = render_to_string(
            "cash_device/receipt_template.html",
            {
                "items": items,
                "total_price": total_price,
                "day_time_now": day_time_now,
                "company_name": "Рога и копыта",
                "kkm": "11111111",
                "inn": "22222222",
            },
        )

        file_name = f"receipt_{int(datetime.now().timestamp())}.pdf"
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)

        #PDF для чека
        pdfkit.from_string(html_information, file_path)

        file_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, file_name))

        #QR Code
        qr_code_url = qrcode.make(file_url)
        qr_filename = f"qr_{file_name}.png"
        qr_path = os.path.join(settings.MEDIA_ROOT, qr_filename)
        qr_code_url.save(qr_path)

        return Response(
            {
                "receipt_pdf": file_url,
                "qr_code": request.build_absolute_uri(os.path.join(settings.MEDIA_URL, f"qr_{file_name}.png")),
            },
            status=status.HTTP_201_CREATED,
        )
