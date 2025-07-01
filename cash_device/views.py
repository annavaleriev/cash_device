from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import CashMachineSerializer
from rest_framework import status
'''
    http://192.168.1.3:8888/cash_machine
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





def view_pdf(request, filename): #/media/1234124124.pdf
    pass
