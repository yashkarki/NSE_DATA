from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from .models import *
from .serializers import DailyPriceSerializer

# Create your views here.



class StockAPI(APIView):
    def get(self,request):
        # data=request.data
        daily_obj=DailyPrice.objects.all()
        serializer = DailyPriceSerializer(daily_obj,many=True)
        # index_name=data['index_name']
        return Response(serializer.data,status.HTTP_200_OK)