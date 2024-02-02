from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from .models import *
from .serializers import DailyPriceSerializer
from django.core.paginator import Paginator


# Create your views here.



class StockAPI(APIView):
    def get(self,request):
        daily_obj=DailyPrice.objects.all()
        serializer = DailyPriceSerializer(daily_obj,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self,request):
        data=request.data
        var_page = data.get('var_page', 1)
        index_name=data.get('index_name')
        start_date=data.get('start_date','')
        end_date=data.get('end_date','')
        open_lowest = data.get('open_lowest')
        open_highest=data.get('open_highest')
        low_lowest = data.get('low_lowest','')
        low_highest = data.get('low_highest','')
        high_lowest = data.get('high_lowest','')
        high_highest = data.get('high_highest','')
        close_lowest = data.get('close_lowest','')
        close_highest = data.get('close_highest','')
        shares_traded_lowest = data.get('shares_traded_lowest','')
        shares_traded_highest = data.get('shares_traded_highest','')
        turnover_lowest = data.get('turnover_lowest','')
        turnover_highest = data.get('turnover_highest','')


        filter_conditions={
            'index__name':index_name,
            'date__gte':start_date,
            'date__lte':end_date,
            'open_price__gte':open_lowest,
            'open_price__lte':open_highest,
            'low_price__gte':low_lowest,
            'low_price__lte':low_highest,
            'high_price__gte':high_lowest,
            'high_price__lte':high_highest,
            'close_price__gte':close_lowest,
            'close_price__lte':close_highest,
            'shares_traded__gte':shares_traded_lowest,
            'shares_traded__lte':shares_traded_highest,
            'turnover__gte':turnover_lowest,
            'turnover__lte':turnover_highest         
        }
        filter_conditions = {
            key: value for key, value in filter_conditions.items() if value}
        daily_obj=DailyPrice.objects.filter(**filter_conditions)
        serializer = DailyPriceSerializer(daily_obj, many=True)
        p = Paginator(serializer.data, 25)
        page_obj = p.get_page(var_page)
        max_page = p.num_pages
        data={
            "start-date":str(start_date),
            "end-date":str(end_date),
            "data":list(page_obj),
            "pagination":{
                "page":var_page,
                "toal_pages":max_page,
                "total_rows":len(daily_obj)
            },
            "ranges":{
                "open":{"lowest":open_lowest,"highest":open_highest},
                "high": {"lowest": high_lowest, "highest": high_highest},
                "low": {"lowest": low_lowest, "highest": low_highest},
                "close": {"lowest": close_lowest, "highest": close_highest},
                "shares_traded": {"lowest": shares_traded_lowest, "highest": shares_traded_highest},
                "turnover": {"lowest": turnover_lowest, "highest": turnover_highest}

            }

        }


        return Response(data,status.HTTP_200_OK)
