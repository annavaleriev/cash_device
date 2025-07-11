from django.http import HttpResponse
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Item
from .serializers import CashMachineSerializer
from .services import PDFReceiptGenerator, QRCodeGenerator


class CashMachineViewSet(CreateModelMixin, GenericViewSet):
    """ViewSet для кассового аппарата, который принимает список товаров и возвращает QR-код с PDF-чеком."""

    serializer_class = CashMachineSerializer
    queryset = Item.objects.all()

    def create(self, request, *args, **kwargs):
        """Обрабатывает POST-запросы для создания чека."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pdf_generator = PDFReceiptGenerator(serializer.validated_data["items"])
        pdf_file = pdf_generator.generate()

        file_url = request.build_absolute_uri(pdf_file.file.url)

        qr_generator = QRCodeGenerator(file_url)
        qr_buffer = qr_generator.generate()

        return HttpResponse(qr_buffer, content_type="image/png")
