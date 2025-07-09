from django.http import HttpResponse
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSet, ModelViewSet

from .models import Item
from .serializers import CashMachineSerializer

from .services import PDFReceiptGenerator, QRCodeGenerator


class CashMachineViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = CashMachineSerializer
    queryset = Item.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pdf_generator = PDFReceiptGenerator(serializer.validated_data["items"])
        pdf_file = pdf_generator.generate()

        qr_generator = QRCodeGenerator(pdf_file.file.url)
        qr = qr_generator.generate()
        return HttpResponse(qr, content_type="image/png")


        # serializer = CashMachineSerializer(data=request.data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #
        # items_id = serializer.validated_data["items"]
        # items = Item.objects.filter(id__in=items_id)
        #
        # total_price = sum(item.price for item in items)
        # day_time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #
        # # html_information = render_to_string(
        # #     "cash_device/receipt_template.html",
        # #     {
        # #         "items": items,
        # #         "total_price": total_price,
        # #         "day_time_now": day_time_now,
        # #     },
        # # )
        # html_information = render_to_string(
        #     "cash_device/receipt_template.html",
        #     {
        #         "items": items,
        #         "total_price": total_price,
        #         "day_time_now": day_time_now,
        #         "company_name": "Рога и копыта",
        #         "kkm": "11111111",
        #         "inn": "22222222",
        #     },
        # )
        #
        # file_name = f"receipt_{int(datetime.now().timestamp())}.pdf"
        # file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        #
        # #PDF для чека
        # pdfkit.from_string(html_information, file_path)
        #
        # file_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, file_name))
        #
        # #QR Code
        # qr_code_url = qrcode.make(file_url)
        # qr_filename = f"qr_{file_name}.png"
        # qr_path = os.path.join(settings.MEDIA_ROOT, qr_filename)
        # qr_code_url.save(qr_path)
        #
        # return Response(
        #     {
        #         "receipt_pdf": file_url,
        #         "qr_code": request.build_absolute_uri(os.path.join(settings.MEDIA_URL, f"qr_{file_name}.png")),
        #     },
        #     status=status.HTTP_201_CREATED,
        # )


# class HelloView(ModelViewSet):
#     def get(self, request):
#         return Response({"message": "Hello, world!"})