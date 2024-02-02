from django.core.management.base import BaseCommand
from tickdata.models import StockIndex, DailyPrice
import pandas as pd
import requests
from io import StringIO



class Command(BaseCommand):
    help = 'Import data into Django models from CSV files which shuld be present in historical_data_by_indices and named as Indices name as in DB'

    def handle(self, *args, **kwargs):
    
        index_list = ["NIFTY_50","NIFTY_NEXT_50", "NIFTY_MIDCAP_50", "NIFTY_MIDCAP_100","NIFTY_MIDCAP_150"]
        for index_name in index_list:
        
            data = pd.read_csv(f'historical_data_by_indices/{index_name}.csv')
            data['Date '] = pd.to_datetime(data['Date '])
            data['Date '] = data['Date '].dt.strftime('%Y-%m-%d')
            for _,row in data.iterrows():
                index, created = StockIndex.objects.get_or_create(
                    name=index_list[0])
                DailyPrice.objects.get_or_create(
                    index=index,
                    date=row['Date '],
                    open_price=row['Open '],
                    high_price=row['High '],
                    low_price=row['Low '],
                    close_price=row['Close '],
                    shares_traded=row['Shares Traded '],
                    turnover=row['Turnover (₹ Cr)']
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
